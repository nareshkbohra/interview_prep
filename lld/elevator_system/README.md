# Problem statement
1. There are multiple floors and multiple elevators.
2. User can make request standing on a floor or inside an elevator.
3. User who are inside elevator should be served by the same elevator.
4. Optimize for the distance travelled by elevator.


## Central decision problems:
1. Who does what? It is clear that there are two systems elevator and some dispatcher, but who does what
   is cumbersome. For simplicity, elevator just takes the request and keep serving those requests.
2. Dispatcher takes request from users and decide which elevator need to take that request and sends it.

```mermaid
flowchart TD

%% User Interactions
user_ext[User external button pressed at floor with direction] --> sys_add_req[ElevatorSystem add request]
user_int[User internal button pressed inside elevator] --> sys_add_int_req[ElevatorSystem add internal request]

%% Elevator System routes requests
sys_add_req --> elevator0[Elevator 0]
sys_add_int_req --> elevator0

%% Elevator Internal Logic
subgraph Elevator0
  stp[step called]
  stp --> check_dir{Current direction}

  %% IDLE logic
  check_dir -->|IDLE| idle_check

  idle_check -->|Up queue not empty| make_up[Set direction UP]
  idle_check -->|Down queue not empty| make_down[Set direction DOWN]
  idle_check -->|Both queues empty| end_idle[Do nothing]

  %% UP logic
  check_dir -->|UP| move_up[Move one floor up]
  move_up --> at_up_req{Current floor in up queue}
  at_up_req -->|Yes| serve_up[Serve and remove up request]
  at_up_req -->|No| end_up[Continue moving]
  move_up -->|Up queue empty after move| to_idle_up[Set direction IDLE]

  %% DOWN logic
  check_dir -->|DOWN| move_down[Move one floor down]
  move_down --> at_down_req{Current floor in down queue}
  at_down_req -->|Yes| serve_down[Serve and remove down request]
  at_down_req -->|No| end_down[Continue moving]
  move_down -->|Down queue empty after move| to_idle_down[Set direction IDLE]
end
```
