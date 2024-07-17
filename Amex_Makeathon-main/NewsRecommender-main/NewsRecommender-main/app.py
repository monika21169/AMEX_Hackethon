from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)

# Load the cleaned data
data_cleaned = pd.read_csv('corpus.csv')  # Make sure the path to your cleaned data file is correct

def recommend_places(data, preferred_type=None, preferred_zone=None, max_budget=None, max_duration=None):
    print(f"Original Data Size: {data.shape}")
    
    if preferred_type:
        data = data[data['Type'].str.contains(preferred_type, case=False, na=False)]
        print(f"After Type Filter ({preferred_type}): {data.shape}")
    
    if preferred_zone:
        data = data[data['Zone'].str.contains(preferred_zone, case=False, na=False)]
        print(f"After Zone Filter ({preferred_zone}): {data.shape}")
    
    if max_budget is not None:
        data = data[data['Entrance Fee in INR'] <= max_budget]
        print(f"After Budget Filter (<= {max_budget} INR): {data.shape}")
    
    if max_duration is not None:
        data = data[data['time needed to visit in hrs'] <= max_duration]
        print(f"After Duration Filter (<= {max_duration} hrs): {data.shape}")
    
    data = data.sort_values(by=['Google review rating', 'Number of google review in lakhs'], ascending=False)
    return data.head(10)

    final_data = data.head(10)
    print(f"Final Data to be sent to template: {final_data}")
    return final_data



@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    # Fetch form data with default values if empty
    preferred_type = request.form.get('type', '').strip()
    preferred_zone = request.form.get('zone', '').strip()
    
    # Safely convert budget and duration to int and float
    budget_input = request.form.get('budget', '0').strip()
    duration_input = request.form.get('duration', '0').strip()
    
    # Default values if conversion fails
    max_budget = int(budget_input) if budget_input.isdigit() else 0
    max_duration = float(duration_input) if duration_input.replace('.', '', 1).isdigit() else 0.0
    
    recommendations = recommend_places(
        data_cleaned,
        preferred_type=preferred_type,
        preferred_zone=preferred_zone,
        max_budget=max_budget,
        max_duration=max_duration
    )
    
    print("Recommendations DataFrame:", recommendations)  # Debug print
    return render_template('recommendations.html', recommendations=recommendations)


if __name__ == '__main__':
    app.run(debug=True)
