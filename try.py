from flask import Flask, request, jsonify
import cx_Oracle


app = Flask(__name__)

# Configure database connection

dsn1 = cx_Oracle.makedsn('localhost', '1521', service_name='XE')
connection = cx_Oracle.connect(user='SYS', password='SH515440t', dsn=dsn1, mode=cx_Oracle.SYSDBA)

# connection = cx_Oracle.connect(user='SYS', password='SH515440t', dsn=dsn1)
# cx_Oracle.init_oracle_client(config_dir="/home/your_username/oracle/your_config_dir")


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
    first_name = request.json['firstName']
    last_name = request.json['lastName']
    id_card = request.json['idCard']
    city = request.json['address']['city']
    street = request.json['address']['street']
    number = request.json['address']['number']
    date_of_birth = request.json['dateOfBirth']
    telephone = request.json['telephone']
    mobile = request.json['mobile']
    vaccine1_date = request.json['coronaVaccines'][0]['date']
    vaccine1_manufacturer = request.json['coronaVaccines'][0]['manufacturer']
    vaccine2_date = request.json['coronaVaccines'][1]['date']
    vaccine2_manufacturer = request.json['coronaVaccines'][1]['manufacturer']
    vaccine3_date = request.json['coronaVaccines'][2]['date']
    vaccine3_manufacturer = request.json['coronaVaccines'][2]['manufacturer']
    vaccine4_date = request.json['coronaVaccines'][3]['date']
    vaccine4_manufacturer = request.json['coronaVaccines'][3]['manufacturer']
    positive_result_date = request.json['coronaPositive']['resultDate']
    recovery_date = request.json['coronaPositive']['recoveryDate']

    with connection.cursor() as cur:
        cur.execute(
            "INSERT INTO employees (first_name, last_name, id_card, city, street, number, date_of_birth, telephone, mobile, vaccine1_date, vaccine1_manufacturer, vaccine2_date, vaccine2_manufacturer, vaccine3_date, vaccine3_manufacturer, vaccine4_date, vaccine4_manufacturer, positive_result_date, recovery_date) VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11, :12, :13, :14, :15, :16, :17, :18, :19)",
            (first_name, last_name, id_card, city, street, number, date_of_birth, telephone, mobile, vaccine1_date, vaccine1_manufacturer, vaccine2_date, vaccine2_manufacturer, vaccine3_date, vaccine3_manufacturer, vaccine4_date, vaccine4_manufacturer, positive_result_date, recovery_date))
    connection.commit()

    return jsonify({'message': 'Employee added successfully.'})


if __name__ == '__main__':
    app.run(debug=True)
