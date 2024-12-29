import time 
from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Initialize a 2D array to represent the parking lot (5x5)
parking_lot = [[False for _ in range(5)] for _ in range(5)]
available_seats = random.sample([(i, j) for i in range(5) for j in range(5)], 10)
global user_amt
user_amt = 10
# parking_lot[2][2] = True

def make_payment():
    # if amt > 0 :
    #     # amt = amt - 5   
    #     return True
    # else:
    #     return False
    return True

def payment(row,col,user_id):
    row = int(row)
    col = int(col)
    user_id = user_id 

    # Check if the seat is still avfind_seatailable
    if parking_lot[row][col]==True:
    # if parking_lot[row][col]=='selected...' :
        # Proceed to payment processing (simulate with a simple check)
        if random.choice([True, False ]):  # Simulate payment success/failure
        # if random.choice([True, False,'selected...' ]):  # Simulate payment success/failure
            # pay= make_payment()  # Update parking lot status after successful payment
            if 1:
                parking_lot[row][col] = {'user_id': user_id, 'paid': True}
                parking_lot[row][col] = True

                return jsonify({'status': 'success', 'message': 'Payment successful'})
            
            else:
                return jsonify({'status': 'Failed' , "message": 'payment failed'})
        else:
            return jsonify({'status': 'failed in payment', 'message': 'in choice'})
    else:
        return jsonify({'status': 'error in clo, row', 'message': 'Seat is no longer available'})
    

@app.route('/')
def index():
    return render_template('index.html', parking=parking_lot )

@app.route('/find_seat', methods=['POST'])
def find_seat():
    username = request.form['username']
    user_id = request.form['user_id']

    # Find an empty seat randomly
    # if False in parking_lot:
    while True:
        row = random.randint(0, 4)
        col = random.randint(0, 4)
        # row = 2
        # col=2
        if not parking_lot[row][col]:
            break
    

    # Assign the seat to the user
    parking_lot[row][col] = True
    # parking_lot[row][col] = 'selected'
    # else:
    #     return jsonify({'status': 'error', 'message': 'Parking lot is full no free space'})
        
    # Return the seat information as JSON
    time.sleep(5)
    return payment(row,col,user_id)


if __name__ == '__main__':
    
    app.run(debug=True)