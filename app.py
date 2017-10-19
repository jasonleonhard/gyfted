"""."""
from flask import render_template, request, session, redirect
from models import app, db, Ticket


@app.route("/")
def index():
    """Splash screen."""
    return render_template("index.html")


@app.route("/about")
def about():
    """Mission statement."""
    return render_template("about.html")


@app.route("/map")
def map():
    """Stubbed out map and list view."""
    return render_template("map.html")


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    """."""
    return render_template('hello.html', name=name)


@app.route('/ticket/')
@app.route('/ticket/<item>')
def ticket(item=None):
    """."""
    return render_template('ticket.html', item=item)


@app.route("/newticket", methods=['POST', 'GET'])
def newticket(item='', deliverer='',
              gyfter='', pickup_address='', pickup_time='', pickup_date='',
              requester='', dropoff_address='', dropoff_time='',
              dropoff_date=''):
    """Stubbed out map and list view."""
    if request.method == 'GET':
        return render_template('newticket.html')  # , title=title)
    if request.method == 'POST':
        # Clear sessions then store form fields in session object by name
        session.clear()
        session['item'] = request.form['item']
        session['deliverer'] = request.form['deliverer']

        session['gyfter'] = request.form['gyfter']
        session['pickup_address'] = request.form['pickup_address']
        session['pickup_time'] = request.form['pickup_time']
        session['pickup_date'] = request.form['pickup_date']

        session['requester'] = request.form['requester']
        session['dropoff_address'] = request.form['dropoff_address']
        session['dropoff_time'] = request.form['dropoff_time']
        session['dropoff_date'] = request.form['dropoff_date']

        # alternative store form fields in varibles & create new ticket object
        item = request.form['item']
        deliverer = request.form['deliverer']

        gyfter = request.form['gyfter']
        pickup_address = request.form['pickup_address']
        pickup_time = request.form['pickup_time']
        pickup_date = request.form['pickup_date']

        requester = request.form['requester']
        dropoff_address = request.form['dropoff_address']
        dropoff_time = request.form['dropoff_time']
        dropoff_date = request.form['dropoff_date']

        ticket = Ticket(item, deliverer, gyfter, pickup_address,
                        pickup_time, pickup_date, requester,
                        dropoff_address, dropoff_time, dropoff_date)

        db.session.add(ticket)
        db.session.commit()
        return render_template('show.html', ticket=ticket)

@app.route("/addticket", methods=['POST', 'GET'])
def addticket(item='', deliverer='',
              gyfter='', pickup_address='', pickup_time='', pickup_date='',
              requester='', dropoff_address='', dropoff_time='',
              dropoff_date=''):
    """Stubbed out map and list view."""
    if request.method == 'GET':
        return render_template('addticket.html')  # , title=title)
    if request.method == 'POST':
        if request.form['formtype']=="donate":
            print(request.form['formtype'])
            item = request.form['item']
            gyfter = request.form['name']
            email = request.form['contactemail']
            pickup_address = request.form['location']
            pickup_time = request.form['time']
            pickup_date = request.form['expiration']
            if request.form['delivery']=='2' :
                deliverer= gyfter

        elif request.form['formtype']=="request": 
            print(request.form['formtype'])
            item = request.form['item']
            requester = request.form['name']
            email = request.form['contactemail']
            dropoff_address = request.form['location']
            dropoff_time = request.form['time']
            dropoff_date = request.form['expiration']
            if request.form['pickup'] == '2' :
                deliverer= requester
            
    ticket = Ticket(item, deliverer, gyfter, pickup_address,
                        pickup_time, pickup_date, requester,
                        dropoff_address, dropoff_time, dropoff_date)

    db.session.add(ticket)
    db.session.commit()
    return render_template('show.html', ticket=ticket) 

@app.route("/show_all", methods=['GET'])
def show_all():
    """Stubbed out show and list users view."""
    all_tickets = Ticket.query.all()
    return render_template('show_all.html', all_tickets=all_tickets)


@app.route('/delete_ticket', methods=['GET', 'POST'])
def delete_ticket():
    """Hide ticket instead of removing from db.

    grabs hidden ticket id from form, queries it and 'deletes' by hiding.
    """
    ticket_id = request.form['tid']  # WIP
    hide_ticket = Ticket.query.get(ticket_id)

    if not hide_ticket:
        return redirect("/?error=Attempt to watch a ticket unknown to db")

    hide_ticket.hidden = True
    db.session.commit()
    return redirect('/show_all')  # currently only


# disable browser caching
@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame.

    Also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)
    app.debug = True
