import streamlit as st

# Your specific workout structure
workout_data = {
    "Warmup (2 min)": ["Skipping Rope"],
    "Explosiveness (3 rounds)": ["Gym ball Squat jumps (3x5)", "Ball Slam Variations (3x5)", "Punching Bag (30 sec)"],
    "Mobility (5 min)": ["Kettlebell Halos (2x10)", "Deep Squats (2x10)", "Dead Hang (2x60s)"],
    "Strength A": {
        "CHEST": ["Bench Press", "Incline Bench Press", "Weighted Dip"],
        "QUADS": ["Front Squat", "Hack Squat", "Cossack Squat", "Split Squat", "Bulgarian Split Squat"],
        "ABS": ["Cable Crunch", "Reverse Cable Crunch", "Hanging Knee Raises"]
    },
    "Strength B": {
        "HAMSTRINGS": ["Sumo Deadlift", "Nordic Curls"],
        "BACK": ["Horizontal Row", "Leuat", "Vertical Row"],
        "ROTATIONAL": ["Landmine 180", "Cable Twists"]
    },
    "Strength C": {
        "CALVES": ["Calf Raises"],
        "PECS": ["Cable Pec Flies"],
        "CORE": ["Pallof Press", "Farmer's Walk"]
    },
    "Strength D": {
        "BACK": ["Face Pulls"],
        "BICEPS": ["Bicep Curls"],
        "DELTS": ["Overhead Press"]
    }
}

st.set_page_config(page_title="My Workout Planner", layout="centered")

st.title("💪 Gym Session Selector")

# Sidebar for selections
with st.sidebar:
    st.header("Select Exercises")
    final_selections = {}
    
    for goal, content in workout_data.items():
        st.subheader(goal)
        if isinstance(content, list):
            # For fixed rounds like Warmup/Mobility, we just keep them all
            final_selections[goal] = content
            st.info("Fixed sequence")
        else:
            # For Strength rounds, let user pick the specific variation
            goal_picks = []
            for category, options in content.items():
                if len(options) > 1:
                    pick = st.selectbox(f"{category}", options, key=f"{goal}_{category}")
                    goal_picks.append(f"{category}: {pick}")
                else:
                    # If only one option exists, auto-add it
                    goal_picks.append(f"{category}: {options[0]}")
            final_selections[goal] = goal_picks

# Main Display
st.header("Today's Program")
for goal, exercises in final_selections.items():
    with st.expander(f"GOAL: {goal}", expanded=True):
        for ex in exercises:
            st.checkbox(ex, key=f"check_{goal}_{ex}")

if st.button("Clear All Checkboxes"):
    st.rerun()
