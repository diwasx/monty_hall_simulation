# Monty Hall Problem Simulation

This Python script simulates the **Monty Hall Problem**, a well-known probability puzzle based on a game show scenario. In this simulation, we calculate the probability of winning a car based on two different strategies: **staying with the initial choice** and **switching the door**.

## Problem Description

In the Monty Hall Problem:
- There are three doors, one of which hides a car while the other two hide goats.
- The player picks a door.
- The host, who knows what's behind each door, opens one of the other two doors to reveal a goat.
- The player then has the option to either stick with their original choice or switch to the remaining unopened door.

The goal is to determine which strategy (staying or switching) offers a higher probability of winning the car.

## How the Code Works

### Simulation Function

1. **`trail()`**: 
   - Sets up the doors, placing the car behind one door at random. The other two doors contain goats.

2. **`winning_probability()`**: 
   - Simulates the scenario where the player sticks with their initial choice. It calculates the probability of winning based on the player's initial selection.

3. **`switch_case(switch)`**:
   - Simulates both cases: when the player switches or stays with their original choice.
   - If `switch=True`, the player switches doors after the host opens one door.
   - If `switch=False`, the player sticks with their initial choice.
   - For each case, the simulation runs multiple trials and calculates the winning probability.

### Parameters

- `n`: Number of trials for the simulation (default is 10,000,000).
- `debug`: Toggle debug mode to print details of each trial (default is `False`).
  
### Example Usage

To simulate the switching case:

```python
switch_case(True)
```

## Results

- When **switching**, the player wins approximately 66.67% of the time.
- When **not switching**, the player wins approximately 33.33% of the time.

This demonstrates that switching doors gives a much higher probability of winning the car than sticking with the initial choice.

## Requirements

- Python 3.x
- No additional libraries required as it uses only the standard `random` module.

## Running the Script

1. Download or clone the repository.
2. Run the script using Python:

    ```bash
    python3 monty_hall.py
    ```

The output will display the winning probabilities after running the simulation for the specified number of trials.

## Customization

- You can adjust the number of trials by changing the value of `n`.
- You can enable `debug` mode to view the intermediate results and details of each trial:

    ```python
    debug = True
    ```

## License

This project is licensed under the MIT License.
