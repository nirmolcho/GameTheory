import streamlit as st
import random
import time
# import pyautogui-enable to auto play bgm music
# Define the strategies
def TitForTat(arr1, arr2, index):
    if index == 0:
        arr1.append(1)
    else:
        arr1.append(arr2[-1])
    return arr1

def AlwaysCooperate(arr1, arr2, index):
    arr1.append(1)
    return arr1

def AlwaysDefect(arr1, arr2, index):
    arr1.append(0)
    return arr1

def Friedman(arr1, arr2, index):
    if index == 0:
        arr1.append(1)
    else:
        if 0 in arr2:
            arr1.append(0)
        else:
            arr1.append(1)
    return arr1

def Joss(arr1, arr2, index):
    if index == 1:
        arr1.append(1)
    else:
        if random.random() < 0.9:
            arr1.append(arr2[-1])
        else:
            arr1.append(0)
    return arr1

def generous_tit_for_tat(arr1, arr2, index):
    if index == 0:
        arr1.append(1)
    else:
        opponent_last_move = arr2[-1]
        if opponent_last_move == 0:
            if random.random() < 0.9:
                arr1.append(0)
            else:
                arr1.append(1)
        else:
            arr1.append(1)
    return arr1

def tit_for_two_tats(arr1, arr2, index):
    if index == 0:
        arr1.append(1)
    elif index == 1:
        arr1.append(1 if arr2[-1] == 1 else 0)
    else:
        if arr2[-1] == 0 and arr2[-2] == 0:
            arr1.append(0)
        else:
            arr1.append(1)
    return arr1

def tester_strategy(arr1, arr2, index):
    if index == 0:
        arr1.append(0)
    elif index == 1:
        arr1.append(1)
    elif index == 2:
        arr1.append(1 if arr2[-1] == 0 else arr2[-1])
    else:
        if arr2[-1] == 0:
            arr1.append(1)
        else:
            arr1.append(0 if index % 2 == 0 else 1)
    return arr1

def play_strategies(strategy1, strategy2, rounds):
    arr1 = []
    arr2 = []
    names = {TitForTat: "TitForTat", AlwaysCooperate: "AlwaysCooperate", AlwaysDefect: "AlwaysDefect",
             Friedman: "Friedman", Joss: "Joss", generous_tit_for_tat: "Generous TitForTat",
             tit_for_two_tats: "TitForTwoTats", tester_strategy: "Tester"}

    for i in range(rounds):
        strategy1(arr1, arr2, i)
        strategy2(arr2, arr1, i)

        # Print strategy names and moves with scores
        st.write(f"Round {i + 1}:")
        st.write(f"Strategy 1 ({names[strategy1]}): {'Cooperate' if arr1[-1] == 1 else 'Not Cooperate'}")
        st.write(f"Strategy 2 ({names[strategy2]}): {'Cooperate' if arr2[-1] == 1 else 'Not Cooperate'}")

        score1, score2 = calculate_scores(arr1, arr2)
        st.write(f"Score for {names[strategy1]}: {score1}")
        st.write(f"Score for {names[strategy2]}: {score2}")
        st.write("---")

        time.sleep(2)  # Wait for 2 seconds before the next round

    return score1, score2

def calculate_scores(arr1, arr2):
    score1 = 0
    score2 = 0
    for move1, move2 in zip(arr1, arr2):
        if move1 == 1 and move2 == 1:
            score1 += 3
            score2 += 3
        elif move1 == 0 and move2 == 0:
            score1 += 1
            score2 += 1
        elif move1 == 1 and move2 == 0:
            score2 += 5
        elif move1 == 0 and move2 == 1:
            score1 += 5
    return score1, score2

def play_user_vs_strategy(user_moves, strategy, rounds):
    user_arr = user_moves[:]
    strategy_arr = []

    names = {TitForTat: "TitForTat", AlwaysCooperate: "AlwaysCooperate", AlwaysDefect: "AlwaysDefect",
             Friedman: "Friedman", Joss: "Joss", generous_tit_for_tat: "Generous TitForTat",
             tit_for_two_tats: "TitForTwoTats", tester_strategy: "Tester"}

    if "round" not in st.session_state:
        st.session_state.round = 0
        st.session_state.strategy_arr = []
        st.session_state.user_arr = user_arr

    current_round = st.session_state.round

    if current_round < rounds:
        st.write(f"Round {current_round + 1}:")

        # User input for the current round
        user_move = st.selectbox("Select your move", [1, 0], key=f"user_move_{current_round}")

        if st.button("Submit Move"):
            st.session_state.user_arr[current_round] = user_move
            strategy(st.session_state.strategy_arr, st.session_state.user_arr, current_round)

            # Get the latest move
            strategy_move = st.session_state.strategy_arr[-1]

            # Calculate scores
            score_user, score_strategy = calculate_scores(st.session_state.user_arr[:current_round + 1], st.session_state.strategy_arr)

            # Display moves and scores for the current round
            st.write(f"User: {'Cooperate' if user_move == 1 else 'Not Cooperate'}")
            st.write(f"Strategy ({names[strategy]}): {'Cooperate' if strategy_move == 1 else 'Not Cooperate'}")
            st.write(f"Score for User: {score_user}")
            st.write(f"Score for {names[strategy]}: {score_strategy}")
            st.write("---")

            # Increment the round counter
            st.session_state.round += 1

            time.sleep(2)  # Wait for 2 seconds before the next round

    if st.session_state.round == rounds:
        # Display final results
        final_score_user, final_score_strategy = calculate_scores(st.session_state.user_arr, st.session_state.strategy_arr)
        st.write(f"Final Score for User: {final_score_user}")
        st.write(f"Final Score for {names[strategy]}: {final_score_strategy}")

        if final_score_user > final_score_strategy:
            st.write("User wins!")
        elif final_score_strategy > final_score_user:
            st.write(f"{names[strategy]} wins!")
        else:
            st.write("It's a tie!")


# Streamlit app
st.set_page_config(page_title="Game Theory", page_icon=":game_die:")
st.write("The Classic Veritasium Music to get things in the Mood🎼")
# pyautogui.press('F4')#whatever key has play button in your keyboard enter that so pyautogui presses that for autoplay of bgm
st.audio("bgm.mp3",loop=True,autoplay=True,start_time=0)
# Sidebar for page navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Simulation", "Play Against Strategy","Strategies Info"])

if page == "Home":
    # Home page
    st.title("Game Theory")
    st.header("Let's play a game!")
    st.video("goldy.mp4", loop=True, start_time=0, autoplay=True, muted=True)

    st.header("Introduction")
    st.write("""
    Game Theory is a field of mathematics that studies strategic interactions among rational decision-makers. 
    It provides a framework for analyzing situations where the outcome depends on the actions of multiple agents, 
    each with their own interests.

    Game theory, through the analysis of strategies, highlights key qualities that contribute to successful outcomes in repeated interactions. These qualities include being "Nice," "Forgiving," "Retaliatory," and "Clear." A strategy that embodies these qualities tends to foster trust, maintain cooperation, discourage exploitation, and create predictable interactions. For instance, a "Nice" strategy promotes initial cooperation, while "Forgiving" allows for the restoration of cooperation after conflict, preventing long-term grudges. Being "Retaliatory" ensures fairness by responding to defection, and "Clear" strategies help in establishing predictable and stable interactions.

    These qualities, which define good strategies in game theory, are equally applicable in real life. Being nice fosters goodwill, forgiveness maintains relationships despite occasional conflicts, retaliation prevents exploitation, and clarity builds trust and predictability. Thus, game theory not only provides insights into strategic interactions but also explains the moral behaviors that underpin successful human relationships.

    In the context of the Iterated Prisoner's Dilemma (IPD), players interact repeatedly over multiple rounds, 
    choosing between cooperation and defection. The game explores the consequences of these choices over time, 
    with various strategies exhibiting different behaviors.

    ### Rules of the Iterated Prisoner's Dilemma:
    1. **Players**: Two players interact repeatedly.
    2. **Choices**: In each round, each player can either:
       - Cooperate with the opponent
       - Defect with the opponent
    3. **Payoff Matrix**:
       - Both Cooperate: Each player gets 3 points.
       - Both Defect: Each player gets 1 point.
       - One Cooperates and the other Defects: The defector gets 5 points, and the cooperator gets 0 points.

    For more information on specific strategies and simulations, check out the interactive simulation provided in this app.
    """)
    st.write("This project was inspired by the video by Veritasium,which speaks in detail about game theory and its applications in life")
    st.write("So make sure to check it our for more details!")
    st.video("https://www.youtube.com/watch?v=mScpHTIi-kM")

elif page == "Simulation":
    # Simulation page
   
    st.write("Select any two strategies to run a simulation and see how they perform against each other.")

    # Strategy selection
    strategy_options = {
        "TitForTat": TitForTat,
        "AlwaysCooperate": AlwaysCooperate,
        "AlwaysDefect": AlwaysDefect,
        "Friedman": Friedman,
        "Joss": Joss,
        "Generous TitForTat": generous_tit_for_tat,
        "TitForTwoTats": tit_for_two_tats,
        "Tester": tester_strategy
    }
    
    strategy1_name = st.selectbox("Select Strategy 1", list(strategy_options.keys()))
    strategy2_name = st.selectbox("Select Strategy 2", list(strategy_options.keys()))
    rounds = st.number_input("Number of Rounds", min_value=1, max_value=100, value=10)

    if st.button("Run Simulation"):
        strategy1 = strategy_options[strategy1_name]
        strategy2 = strategy_options[strategy2_name]

        st.write(f"Running simulation between {strategy1_name} and {strategy2_name} for {rounds} rounds...")
        score1, score2 = play_strategies(strategy1, strategy2, rounds)
        
        st.write(f"Final Score for {strategy1_name}: {score1}")
        st.write(f"Final Score for {strategy2_name}: {score2}")
        st.write("---")
        
        if score1 > score2:
            st.write(f"{strategy1_name} wins!")
        elif score2 > score1:
            st.write(f"{strategy2_name} wins!")
        else:
            st.write("It's a tie!")
elif page == "Play Against Strategy":
    # Play Against Strategy page
    st.title("Play Against a Strategy")

    strategy_options = {
        "TitForTat": TitForTat,
        "AlwaysCooperate": AlwaysCooperate,
        "AlwaysDefect": AlwaysDefect,
        "Friedman": Friedman,
        "Joss": Joss,
        "Generous TitForTat": generous_tit_for_tat,
        "TitForTwoTats": tit_for_two_tats,
        "Tester": tester_strategy
    }

    strategy_name = st.selectbox("Select Strategy to Play Against", list(strategy_options.keys()))
    rounds = st.number_input("Number of Rounds", min_value=1, max_value=100, value=10)
    strategy = strategy_options[strategy_name]

    # Initialize session state
    if "user_moves" not in st.session_state:
        st.session_state.user_moves = []
    if "current_round" not in st.session_state:
        st.session_state.current_round = 0
    if "strategy_moves" not in st.session_state:
        st.session_state.strategy_moves = []
    if "user_score" not in st.session_state:
        st.session_state.user_score = 0
    if "strategy_score" not in st.session_state:
        st.session_state.strategy_score = 0

    if st.session_state.current_round < rounds:
        # User input for the current round
        user_move = st.selectbox(
            f"Round {st.session_state.current_round + 1} Move", 
            ["Choose your option", "Cooperate", "Not Cooperate"], 
            key=f"user_move_{st.session_state.current_round}"
        )
        
        if user_move != "Choose your option" and st.button("Submit Move"):
            # Convert user move to binary
            user_move_binary = 1 if user_move == "Cooperate" else 0
            
            # Add user's move to the list
            st.session_state.user_moves.append(user_move_binary)
            
            # Generate strategy's move
            strategy(st.session_state.strategy_moves, st.session_state.user_moves, st.session_state.current_round)
            
            # Get the latest move
            strategy_move = st.session_state.strategy_moves[-1]
            
            # Calculate scores
            if user_move_binary == 1 and strategy_move == 1:
                st.session_state.user_score += 3
                st.session_state.strategy_score += 3
            elif user_move_binary == 0 and strategy_move == 0:
                st.session_state.user_score += 1
                st.session_state.strategy_score += 1
            elif user_move_binary == 1 and strategy_move == 0:
                st.session_state.strategy_score += 5
            elif user_move_binary == 0 and strategy_move == 1:
                st.session_state.user_score += 5

            # Display moves and scores for the current round
            st.write(f"Round {st.session_state.current_round + 1}:")
            st.write(f"User: {user_move}")
            st.write(f"Strategy ({strategy_name}): {'Cooperate' if strategy_move == 1 else 'Not Cooperate'}")
            st.write(f"Score for User: {st.session_state.user_score}")
            st.write(f"Score for {strategy_name}: {st.session_state.strategy_score}")
            st.write("---")
            
            # Increment the round counter
            st.session_state.current_round += 1

            time.sleep(2)  # Wait for 2 seconds before the next round

    if st.session_state.current_round == rounds:
        # Display final results
        st.write(f"Final Score for User: {st.session_state.user_score}")
        st.write(f"Final Score for {strategy_name}: {st.session_state.strategy_score}")
        
        if st.session_state.user_score > st.session_state.strategy_score:
            st.write("User wins!")
        elif st.session_state.strategy_score > st.session_state.user_score:
            st.write(f"{strategy_name} wins!")
        else:
            st.write("It's a tie!")

elif page == "Strategies Info":
    st.title("Strategies Information")

    st.write("**What makes a good stratergy?**")
    st.write("""
Game theory, through the analysis of strategies, highlights key qualities that contribute to successful outcomes in repeated interactions. These qualities include being "Nice," "Forgiving," "Retaliatory," and "Clear." A strategy that embodies these qualities tends to foster trust, maintain cooperation, discourage exploitation, and create predictable interactions. For instance, a "Nice" strategy promotes initial cooperation, while "Forgiving" allows for the restoration of cooperation after conflict, preventing long-term grudges. Being "Retaliatory" ensures fairness by responding to defection, and "Clear" strategies help in establishing predictable and stable interactions.

These qualities, which define good strategies in game theory, are equally applicable in real life. Being nice fosters goodwill, forgiveness maintains relationships despite occasional conflicts, retaliation prevents exploitation, and clarity builds trust and predictability. Thus, game theory not only provides insights into strategic interactions but also explains the moral behaviors that underpin successful human relationships.

Generous TitForTat and TitForTat are among the recognized strategies that exemplify these qualities.
""")
    st.image("qual.jpeg")

    st.write("**TitForTat**: This strategy cooperates initially and then mimics the opponent's last move. If the opponent cooperates, it continues to cooperate; if the opponent defects, it defects in the next round.")

    st.write("**AlwaysCooperate**: This strategy always chooses to cooperate, regardless of the opponent's actions. It aims to consistently build a cooperative relationship.")

    st.write("**AlwaysDefect**: This strategy always chooses to defect, regardless of the opponent's actions. It never cooperates and aims to maximize personal gain by exploiting the opponent's cooperation.")

    st.write("**Friedman**: This strategy cooperates initially and continues to cooperate as long as the opponent does not defect. If the opponent defects, Friedman will switch to defecting in subsequent rounds.")

    st.write("**Joss**: This strategy starts by cooperating. It then follows the opponent's last move most of the time but occasionally defects with a 10% probability to avoid exploitation by more predictable strategies.")

    st.write("**Generous TitForTat**: This strategy cooperates initially and then mimics the opponent's last move, but it forgives a defection with a 10% probability to encourage long-term cooperation.")

    st.write("**TitForTwoTats**: This strategy cooperates initially and continues to cooperate unless the opponent has defected in the last two rounds, in which case it defects. It is more forgiving than TitForTat.")

    st.write("**Tester**: This strategy uses a mix of predefined rules to decide moves. It defects in the first round, cooperates in the second, and then chooses moves based on the opponent's last move and the round index. Specifically, it cooperates if the opponent defected last; otherwise, it alternates between cooperating and defecting depending on whether the round index is even or odd.")

    
