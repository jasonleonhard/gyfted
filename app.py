"""."""
from flask import render_template, request, session, redirect
from models import app, db, Ticket


@app.route("/")
def index():
    """Splash screen."""
    return render_template("index.html", title="Home")


@app.route("/about")
def about():
    """Mission statement."""
    return render_template("about.html", title="About")


@app.route("/map")
def map():
    """Stubbed out map and list view."""
    return render_template("map.html", title="Offerings")


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
    """render ticket form."""
    if request.method == 'GET':
        return render_template('newticket.html', title="New Ticket")  # , title=title)
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

        ticket_id = str(ticket.tid)

        # return render_template('show.html', ticket=ticket)
        return redirect("show_all?tid=" + ticket_id)


@app.route("/show_all", methods=['GET', 'POST'])
def show_all():
    """Stubbed out show and list users view."""

    ticket_id = request.args.get('tid')

    if ticket_id:
        ticket = Ticket.query.get(ticket_id)
        return render_template("showTicket.html", title="View Ticket", ticket=ticket)

    all_tickets = Ticket.query.all()
    return render_template('show_all.html', all_tickets=all_tickets, title="Tickets")


@app.route("/status", methods=['GET', 'POST'])
def status():
    """Stubbed out show and list users view."""

    ticket_id = request.args.get('tid')
    ticket_status = request.args.get('status')
    print("id: ", ticket_id, "status: ", ticket_status)
    ticket = Ticket.query.get(ticket_id)

    if ticket_status == "new":
        return render_template("status_new.html", title="Edit Ticket", ticket=ticket)

    if ticket_status == "ready":

        # retrieve form data
        deliverer = request.form['deliverer']
        requester = request.form['requester']
        dropoff_address = request.form['dropoff_address']
        dropoff_time = request.form['dropoff_time']
        dropoff_date = request.form['dropoff_date']

        # update ticket in db
        ticket.deliverer = deliverer
        ticket.requester = requester
        ticket.dropoff_address = dropoff_address
        ticket.dropoff_time = dropoff_time
        ticket.dropoff_date = dropoff_date
        ticket.status = "ready"
        db.session.commit()

        return redirect("show_all?tid=" + ticket_id)


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
