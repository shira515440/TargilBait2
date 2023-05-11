from flask import Flask, request, jsonify
import cx_Oracle

app = Flask(__name__)

# Configure database connection
dsn1 = cx_Oracle.makedsn('localhost', '1521', service_name='XE')
connection = cx_Oracle.connect(user='SYS', password='SH515440t', dsn=dsn1, mode=cx_Oracle.SYSDBA)


# Route to get all employees
@app.route('/employees', methods=['GET'])
def get_employees():
    with connection.cursor() as cur:
        cur.execute('SELECT * FROM employees')
        employees = cur.fetchall()
    return jsonify(employees)


# Route to add a new employee
@app.route('/employees', methods=['POST'])
def add_employee():

    try:
        e_id = request.json['e_id']
        first_name = request.json['first_name']
        last_name = request.json['last_name']
        id_card = request.json['id_card']
        city = request.json['city']
        street = request.json['street']
        s_number = request.json['s_number']
        date_of_birth = request.json['date_of_birth']
        telephone = request.json['telephone']
        mobile = request.json['mobile']
        vaccine1_date = request.json['vaccine1_date']
        vaccine1_manufacturer = request.json['vaccine1_manufacturer']
        vaccine2_date = request.json['vaccine2_date']
        vaccine2_manufacturer = request.json['vaccine2_manufacturer']
        vaccine3_date = request.json['vaccine3_date']
        vaccine3_manufacturer = request.json['vaccine3_manufacturer']
        vaccine4_date = request.json['vaccine4_date']
        vaccine4_manufacturer = request.json['vaccine4_manufacturer']
        positive_result_date = request.json['positive_result_date']
        recovery_date = request.json['recovery_date']

        with connection.cursor() as cur:
            sql = "INSERT INTO employees (e_id, first_name, last_name, id_card, city, street, s_number, date_of_birth, telephone, mobile, vaccine1_date, vaccine1_manufacturer, vaccine2_date, vaccine2_manufacturer, vaccine3_date, vaccine3_manufacturer, vaccine4_date, vaccine4_manufacturer, positive_result_date, recovery_date) VALUES (:1, :2, :3, :4, :5, :6, :7, TO_DATE(:8, 'YYYY-MM-DD'), :9, :10, TO_DATE(:11, 'YYYY-MM-DD'), :12, TO_DATE(:13, 'YYYY-MM-DD'), :14, TO_DATE(:15, 'YYYY-MM-DD'), :16, TO_DATE(:17, 'YYYY-MM-DD'), :18,TO_DATE(:19, 'YYYY-MM-DD'), TO_DATE(:20, 'YYYY-MM-DD'))"

            values = [e_id, first_name, last_name, id_card, city, street, s_number, date_of_birth, telephone, mobile,
                      vaccine1_date, vaccine1_manufacturer, vaccine2_date, vaccine2_manufacturer, vaccine3_date,
                      vaccine3_manufacturer, vaccine4_date, vaccine4_manufacturer, positive_result_date, recovery_date]
            cur.execute(sql,values)
            connection.commit()


        return jsonify({'message': 'Employee added successfully.'})
        # existing code to get employee data and insert into the database
    except cx_Oracle.DatabaseError as e:
        # handle the exception here
        print("Error: ", e)
        return "Error occurred while adding employee"



if __name__ == '__main__':
    app.run(debug=True)

"""
{

    "e_id": 212591770,
    "first_name": "John",
    "last_name": "Doe",
    "id_card": "123456789",
    "city": "New York",
    "street": "Main St",
    "s_number": "123",
    "date_of_birth": "01-01-1980",
    "telephone": "1234567890",
    "mobile": "9876543210",
    "vaccine1_date": "05-11-2022",
    "vaccine1_manufacturer": "Pfizer",
    "vaccine2_date": "05-01-2022",
    "vaccine2_manufacturer": "Moderna",
    "vaccine3_date": "05-11-2022",
    "vaccine3_manufacturer": "Pfizer",
    "vaccine4_date": "05-01-2022",
    "vaccine4_manufacturer": "Moderna",
    "positive_result_date": "04-01-2022",
    "recovery_date": "04-12-2022"
    
     
}
"""
