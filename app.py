from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Load items from the file
with open(f'Spin-Anime-To-Watch/anime.txt', 'r', encoding='utf-8') as file:
    items = [line.strip() for line in file]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        num_randomize = int(request.form.get('num_randomize'))

        # Perform randomization
        randomized_list = random.sample(items, num_randomize)
        selected_item = randomized_list[-1]  # Get the last item as the final selected item

        return jsonify({'randomized_list': randomized_list, 'selected_item': selected_item})

    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=5002)
