from flask import Flask,render_template, request
from forms import SignupForm, tenantForm, dmvpnForm, csvForm
from aciscript import createTenant
from dmvpn import dmvpn
import dmvpn
import esiaci
from esiaci import inventoryFile, userBuildTenant, acilogin, buildContract, buildPhy, dynamicpool, bdSubnet, buildAep, buildFilter, epgs, buildApp, buildVrf, buildTenant, userBuildTenant
import os
from werkzeug.utils import secure_filename


UPLOAD_FOLDER = '/root/automation/Flask-Site/uploads'


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.secret_key = "development-key"


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignupForm()

    if request.method == 'POST':
        if form.validate() == False:
            return render_template("signup.html", form=form)
        else:
	    return "Success!"
    elif request.method == "GET":
        return render_template("signup.html", form=form)

@app.route("/tenant", methods=["GET", "POST"])
def tenant():
    form = tenantForm()

    tn = form.tenant_name.data
    
    if request.method == 'POST':
        if form.validate() == False:
            return render_template("tenantform.html", form=form)
        else:
             tn_response = createTenant(tn)
             return render_template("tenantform.html", form=form, tnresponse=tn_response)

    elif request.method == "GET":
        return render_template("tenantform.html", form=form)
@app.route("/bd", methods=["GET", "POST"])
def bd():
    form = bdForm()

    bdv = form.bdname.data

    if request.method == 'POST':
        if form.validate() == False:
            return render_template("bdform.html", form=form)
        else:
             tn_response = createBd(bdv)
             return "Created {}".format(bdv)

    elif request.method == "GET":
        return render_template("bdform.html", form=form)

@app.route("/test", methods=["GET", "POST"])
def test():
    return render_template("test.html")


@app.route("/dmvpn", methods=["GET", "POST"])
def dmvpn():
    form = dmvpnForm()

    dop = form.dev_prod.data
    loc = form.data_center.data
    sp = form.service_type.data
    

    if request.method == 'POST':
        if form.validate() == False:
            return render_template("dmvpn.html", form=form)
        else:
             dmvpn_response = dmvpn(dop, loc, sp)
             return render_template("dmvpn.html", form=form, dmvpnresponse=dmvpn_response)

    elif request.method == "GET":
        return render_template("dmvpn.html", form=form)




@app.route("/vpool", methods=["GET", "POST"])
def vpool():
    form = poolForm()

    pn = form.pool_name.data

    if request.method == 'POST':
        if form.validate() == False:
            return render_template("poolform.html", form=form)
        else:
             p_response = createPool(pn)
             return render_template("poolform.html", form=form, pnresponse=pn_response)

    elif request.method == "GET":
        return render_template("poolform.html", form=form)






@app.route("/csvscript", methods=["GET", "POST"])
def createcsv():
    form = csvForm()
    if request.method == 'POST':
	filename = UPLOAD_FOLDER + '/' + form.csv_file.data.filename
	form.csv_file.data.save(filename)
        inventoryFile(filename)   
#me)    if form.csv_file.data:
#            obj = request.files[form.csv_file.name].read()
#            open(os.path.join(UPLOAD_FOLDER, form.csv_file.data), 'w').write(obj)
#            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#            file.save(os.path.join(app.config['UPLOAD_FOLDER'], obj))
    elif request.method == "GET":
        return render_template("csvform.html", form=form)


if __name__ == "__main__":
    app.run(host='10.0.2.15',debug=True)


