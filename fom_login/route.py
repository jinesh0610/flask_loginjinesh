from fom_login import app, db, becrypt
from flask import render_template, redirect, url_for, request, flash
from fom_login.forms import RegistrationForm, LoginForm
from fom_login.model import User
from flask_login import login_user, logout_user, current_user,login_required


@app.route("/")
def home():
    return render_template('home.html',title='home')

@app.route("/thank-you")
def success():
    return render_template("success.html", tittle='success')


@app.route("/account")
@login_required
def account():
    return render_template("account.html", tittle='account')



@app.route("/register", methods=["POST", "GET"])
def sign_up():
    if current_user.is_authenticated:
        return redirect(url_for("account"))
    form = RegistrationForm()
    if form.validate_on_submit():
        encrypt_password = becrypt.generate_password_hash(form.password.data).decode("utf-8")
        user = User(name = form.name.data, email = form.email_id.data,password= encrypt_password)
        db.session.add(user)
        db.session.commit()
        flash(f"Registration for {form.name.data} account is Successfull Now you can login with your email & password", category="success")
        return redirect(url_for("login"))
    return render_template("registerform.html", title="register", form=form)


@app.route("/login", methods = ["POST", "GET"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("account"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email= form.email_id.data).first()
        if user and becrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash(f"Succesfully login for {form.email_id.data} account", category="success")
            return redirect(url_for("account"))
        else:
            flash(f"Unsuccessfully attempt for {form.email_id.data} account", category="danger")
    return render_template("login.html", tittle='login', form = form)

@app.route("/logout")
def logout():
    logout_user()
    flash(f"Logout Successfully", category="success")
    return redirect(url_for("login"))