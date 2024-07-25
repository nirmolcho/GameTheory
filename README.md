# What Game Theory Reveals About Life, The Universe, and Everything

## Overview

This application allows users to explore and simulate various game theory strategies within the Iterated Prisoner's Dilemma (IPD) framework. Users can run simulations to compare how different strategies perform against each other or play against a chosen strategy. The application features an interactive interface for selecting strategies, entering moves, and viewing results.

## About Game Theory

The Iterated Prisoner's Dilemma (IPD) is a classic scenario in game theory that explores the dynamics of cooperation and conflict over multiple rounds of interaction. In the IPD, two players engage in repeated encounters, choosing each round between cooperation and defection. The game's payoff matrix incentivizes both players to act in their own self-interest, but the repeated nature of the game allows for the development of strategies that can build trust and foster long-term cooperation.

Game theory provides a framework for analyzing scenarios where the outcome is influenced by the actions of multiple agents, each with their own interests. It examines how different strategies can lead to successful interactions in repeated settings. Key qualities that contribute to effective strategies in game theory include being "Nice," which involves promoting initial cooperation; "Forgiving," which allows for the restoration of cooperation after conflict; "Retaliatory," which ensures fairness by responding to defection; and "Clear," which helps establish predictable and stable interactions. These principles are not only crucial for successful strategies in theoretical models but also resonate with real-life interactions. Being nice fosters goodwill, forgiveness maintains relationships, retaliation prevents exploitation, and clarity builds trust and predictability. Through the lens of game theory, these qualities illuminate the moral behaviors that underpin successful human relationships and interactions.

## Features

### Home
- **Introduction to Game Theory**: Provides a background on game theory, particularly the Iterated Prisoner's Dilemma (IPD). The page explains the game's rules, including the payoff matrix and the qualities of effective strategies.
- **Inspirational Content**: Features videos that explain and elaborate on the concepts of game theory.

### Simulation
- **Strategy Selection**: Choose two strategies to run a simulation against each other.
- **Round Settings**: Specify the number of rounds for the simulation.
- **Results**: Displays the results of each round, including individual moves and scores, with a summary of final scores to determine the winning strategy.

### Play Against Strategy
- **User Interaction**: Play against a selected strategy by entering your moves for each round.
- **Strategy Selection**: Choose a strategy that you want to play against.
- **Round Settings**: Specify the number of rounds for the game.
- **Real-Time Updates**: View your move, the strategy's move, and scores in real-time for each round, with final results displayed after all rounds are completed.

### Strategies Info
- **Detailed Descriptions**: Learn about the different strategies available in the application, including:
  - **TitForTat**: Cooperates initially and then mimics the opponent's last move.
  - **AlwaysCooperate**: Always cooperates regardless of the opponent's actions.
  - **AlwaysDefect**: Always defects regardless of the opponent's actions.
  - **Friedman**: Cooperates initially and continues unless the opponent defects.
  - **Joss**: Starts by cooperating and mimics the opponent’s last move, with occasional defections.
  - **Generous TitForTat**: Cooperates initially and mimics the opponent's last move, with occasional forgiveness.
  - **TitForTwoTats**: Cooperates initially and continues unless the opponent has defected in the last two rounds.
  - **Tester**: Uses a mix of predefined rules and adapts based on the opponent’s last move.

## Setup

1. **Install Dependencies**: Ensure you have Streamlit installed. You can install them via pip:
    ```bash
    pip install streamlit 
    ```
2. **Run the Application**: Start the Streamlit app by running:
    ```bash
    streamlit run game_theory.py
    ```

## Usage

- **Home Page**: Navigate to get an introduction to game theory and watch related content.
- **Simulation Page**: Select two strategies, set the number of rounds, and run the simulation to compare their performance.
- **Play Against Strategy Page**: Choose a strategy to play against, enter your moves, and see how you fare against the selected strategy.
- **Strategies Info Page**: Read detailed descriptions of the strategies used in the application.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Inspired by [Veritasium`s Video Of Game Theory](https://youtu.be/mScpHTIi-kM?si=ZoihaPKaeyHJABXY).
- Uses Streamlit for interactive web applications.

## Contribution

Feel free to contribute to the project by submitting issues or pull requests. Contributions are welcome!
