from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('app.html')


@app.route('/send', methods=['POST'])
def send(sum=sum):
    if request.method == 'POST':
        num1 = request.form['num1']
        num2 = request.form['num2']
        City = request.form['City']

        if City == 'Riyadh':
            sum = int(num1)*int((float(num2)//40.079))
            return render_template('app.html', sum=sum)

        elif City == 'Buraydah':
            sum = int(num1)*int((float(num2)//36.811))
            return render_template('app.html', sum=sum)

        elif City == 'Ar Rass':
            sum = int(num1)*int((float(num2)//39.052))
            return render_template('app.html', sum=sum)

        elif City == 'Al-Qassim Province':
            sum = int(num1)*int((float(num2)//43.676))
            return render_template('app.html', sum=sum)
        elif City == 'Al-Qassim':
            sum = int(num1)*int((float(num2)//37.221))
            return render_template('app.html', sum=sum)
        elif City == 'Al Bukhariyah':
            sum = int(num1)*int((float(num2)//30.65))
            return render_template('app.html', sum=sum)
        else:
            return render_template('app.html')


if __name__ == ' __main__':
    app.debug = True
    app.run()