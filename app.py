from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    input_val = request.args.get('number', '').strip().upper()
    base_from = request.args.get('base_from', type=int)
    base_to = request.args.get('base_to', type=int)
    result = None
    error = None

    if input_val and base_from and base_to:
        try:
            decimal_value = int(input_val, base_from)
            if decimal_value > 1_000_000_000:
                raise ValueError("Liczba jest zbyt duża!")
            
            if base_to == 10:
                result = str(decimal_value)
            elif base_to == 2:
                result = bin(decimal_value)[2:]
            elif base_to == 16:
                result = hex(decimal_value)[2:].upper()
        except ValueError:
            error = f"Błąd! '{input_val}' to nie jest poprawna liczba w systemie {base_from}."

    return render_template('index.html', result=result, error=error, input_val=input_val, base_from=base_from, base_to=base_to)

import os [cite: 5]

if __name__ == '__main__':
    # Pobiera port ze zmiennej środowiskowej lub używa 5000 jako domyślny lokalnie
    port = int(os.environ.get("PORT", 5000)) [cite: 5]
    # Wyłączenie debug=True na produkcji jest dobrą praktyką bezpieczeństwa
    app.run(host='0.0.0.0', port=port) [cite: 5]