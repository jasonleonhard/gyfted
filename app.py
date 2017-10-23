"""Main gyfted logic and point that is used to start the app."""
from flask import render_template, request, session, redirect
from models import app, db, Ticket
import geocoder
import geopy.distance
from geojson import Point


@app.route('/map2/<int:tid>', methods=['GET', 'POST'])
def map2(tid):
    """Map, list and sentence view for tickets using tid.

    Get ticket id from url, use that to find the ticket
    convert ticket addresses to geolocation and show them
    and finally provide distance calulations.
    """
    tid = tid
    ticket = Ticket.query.get(tid)
    pickup_address = ticket.pickup_address
    dropoff_address = ticket.dropoff_address

    pickup_ll = geocoder.google(pickup_address)
    dropoff_ll = geocoder.google(dropoff_address)

    pickup_geoj = pickup_ll.geojson
    dropoff_geoj = dropoff_ll.geojson

    # complete address
    pickup_address = pickup_geoj['properties']['address']
    dropoff_address = dropoff_geoj['properties']['address']

    p_lat, p_lng = pickup_ll.lat, pickup_ll.lng
    d_lat, d_lng = dropoff_ll.lat, dropoff_ll.lng

    coords_1 = (p_lat, p_lng)
    coords_2 = (d_lat, d_lng)

    dist = geopy.distance.vincenty(coords_1, coords_2).mi
    dist = round(dist, 2)
    dist = str(dist) + ' mi'

    return render_template('map2.html',
                           ticket=ticket,
                           p_lat=p_lat, p_lng=p_lng,
                           d_lat=d_lat, d_lng=d_lng,
                           pickup_geoj=pickup_geoj,
                           dropoff_geoj=dropoff_geoj, dist=dist)


@app.route('/point_2_geojson', methods=['GET', 'POST'])
def point_2_geojson():
    """Return a string of the Point from geojson. Must be string returned."""
    return str(Point((-122.67752, 45.51862))["coordinates"])
    # >> [-122.67752, 45.51862]


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
    """Add headers to both force latest IE rendering engine or Chrome Frame.

    Also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)
    app.debug = True
