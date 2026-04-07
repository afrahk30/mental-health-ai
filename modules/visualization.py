import plotly.express as px

def plot_mood_trend(df):
    df['date'] = df['date'].astype(str)
    fig = px.line(df, x='date', y='score', title="Mood Score Over Time")
    return fig

def plot_emotions(df):
    fig = px.histogram(df, x="emotion", title="Emotion Distribution")
    return fig