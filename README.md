# **Ecommerce Site Project**


This project was built for the purposes of one of my personal projects ("milestone projects") at Code Institute.

This was a Django full stack project, to achieve the following:

>Build a Django project backend by a relational database to create a website that allows users to store and manipulate data records about a particular domain.

Or, slightly more specifically:

>- build a full-stack site based around business logic used to control a centrally-owned dataset
>- set up an authentication mechanism and provide paid access to the site's data and/or other activities based on the dataset, such as the purchase of a product/service

Two other important points were:
- using a relational database (recommending MySQL or Postgres)
- using Stripe payments (naturally using Stripe's test functionality, rather than actual live payments)

The project is built on the basis of and following the tutorial project shown as a part of the course, the main differences 
being the "subject", so to speak - I chose to try and do an online bookstore; and my attempt at using Bulma (the tutorial uses Bootstrap).

---

## Table of Contents
1. [**Design and Features**](#design-and-features)
    - [**Project Purpose**](#project-purpose)
    - [**Design**](#design)
        - [**_Fonts_**](#fonts)
        - [**_Images and Colors_**](#images-and-colors)
        - [**_Navigation_**](#navigation)
        - [**_Responsive Design_**](#responsive-design)
2. [**Technologies Used**](#technologies-used)
3. [**Testing, Features Left to Implement, and Deployment**](#testing-features-left-to-implement-and-deployment)
    - [**Testing**](#testing)
        - [**Deployment**](#deployment)
            - [**Local Deployment**](#local-deployment)
            - [**Remote Deployment**](#remote-deployment)
4. [**Credits**](#credits)
    - [**Content**](#content)
    - [**Media**](#media)
    - [**Acknowledgements**](#acknowledgements)

---

## **Design and Features**

### **Project Purpose**

In addition to what was already mentioned above - in a nutshell: building an ecommerce site
using Django, further focus and emphasis is to be placed on

- a multiple apps structure
    - to be composed of multiple apps, each ideally reusable (an app for each potentially reusable component of the project))

- user authentication & interaction
    - include an authentication mechanism allowing a user to register and log in (plus some motivation - i.e. a reason - fo a user to do so)
    - include at least one form with validation that will enable users to create to interact with the site (edit models in the backend)
In other words:

>create functionality for users to create, locate, display, edit and delete records

and also hopefully do that in a both visually appealing and user friendly manner (ease of use).


### **Design**

#### **_Fonts_**

Site uses two fonts:
 - `Caveat Brush`
 - `Dekko`

 They're chosen as a pair because they work well together, and guided by the general idea to make the site more unassuming and
 less "business-y", with more of like a playful, informal, friedlier note.
 General guiding idea was to use `Dekko` as a font that would increase readability, when compared to `Caveat Brush`: although the
 latter seems more "interesting" and "fun", some of its variants - like its bold rendition with an increased font size - might hinder
 readability.
 So, for instance, `Dekko` might be used for something as a product's (i.e. book's) title; while `Caveat Brush` "looks more interesting" on a navbar.


#### **_Images and Colors_**

 There is basically only two images used that are not products images themselves: the background and the logo.
 Following what is described about the fonts, imagery used tries to follow suite in being less "stern". 

 Colors used as mainly black and white - or rather a "black-looking" specific shade of grey, taken from Bulma's documentation,
 called "Grey dark" there. "Bulma Grey dark" is used to also match some of Bulma's tooltips used. There are also some "neon" effects added to the white color, for instance when howering over certain `<a>` elements.
 Those colors are chosen to be "simple", work well together while having a high-contrast relation between themselves, and also work
 well with the background. 

 There's a favicon implemented as well - the same one as is used for the site's logo.

#### **_Navigation_**

Navbar consist of a site title/logo, which also functions as a home button, and three other elements: a search bar, a view bag button, 
and a log-in (sign-up or sign-in) button.

There are some animations inplemented, to hopefully help the user better understand what's going on. The view bag button has
a items counter - which displays the total number of items it the bag. That counter works in connection with the add-to-bag button
on the product detail page(s): add-to-bag button has a little "+" icon, that when the button is clicked, "jumps" into the bag, thus
signaling to the user the additon when succesfully performed, and also directing attention to the bag items counter, which has now incremented.

The home/index page also has animation that is triggered when the user hovers over "Browse The Books!" button: a beating heart appears under that button.
The idea is something along the lines of "books make our hearts beat"; or "our heart beats for books"; or, simply, "we love books", we love browsing through
books, we love buying books, etc. The heart animation is also my sort of a tribute to https://www.freecodecamp.org/, which I love.

There is also a back-to-top button that appears on the products page when a user scrolls down past a certain point.

#### **_Responsive Design_**

The project basically is built using Bulma, and it tries to utilize Bulma's responsive design ideas and structures.
A few words here also on why Bulma is chosen: mainly, the tutorial project uses Bootstrap, and I wanted to try and step always
and set myself apart from that and use a different CSS framework; I never used Bulma before, and I wanted to try it.

(Although, not using Bootstrap in this particular instance had its own caveats, namely in regards to "crispy forms", buta bit more on that below.)

Main feature on smaller screen, basically, as opposed to the desktop view, is that the navbar condenses into a hamburger menu:
the logo/home button always remains visible, while the rest of the navbar's elements become contained in the hamburger menu.

When actual products are displayed, there are sorted random - each time the page is reloaded, they are reshuffled. The idea behind that is
that in this way no particular product is prioritized by being always displyed first, which could be the case if the products where displayed being ordered
alphabetically by book title or author name, or by SKU, and it makes the page look somewhat different every time. There are some trade-offs though - for instance,
maybe on certain occassions the user would like to quickly return exactly to the spot where he has been previously - to quickly find an item he has already see at a 
certain spot, for instance; by using a radnomized display like this, that item is most likely not to be there anymore where the user saw it.


## **Technologies Used**

- **_IDE and code storage_**
    - GitPod - used as the online IDE
    - GitHub - for the storage of the code online

- **_Full-stack framework_**
    - Django
        - list of installs is in requirements.txt

- **_Database_**
    - Postgres when deployed
    - Django's db.sqlite3 during development

- **_Front-End_**
    - HTML
    - CSS
        - Font Awesome
        - Google Fonts
        - Chrome DevTools
    - JavaScript
        - jQuery

- **_Deployment_**
    - Heroku
    - AWS

## **Testing, Features Left to Implement, and Deployment**

### **Testing**

Apart from manual testing as the project was buing built:

- [HTML Validator](https://validator.w3.org/)
- [CSS Validator](https://jigsaw.w3.org/css-validator/)
- [JSHint](https://jshint.com/)
- [PEP8](http://pep8online.com/)

The project is unfinished: `Stripe` integration plus notification emails setup needs finishing, as well as the Profiles app bit, and the CRUD functionality
for superusers.

There are still some residual Bulma-inherited stylings for certain pesudo-states on certain elements.

The tutorial project makes use of "crispy-forms" in connection with Bootstrap. I tried using the Bulma equivalent, but, as
it clearly warned here (https://pypi.org/project/django-crispy-bulma/)

>This project is an early work in progress. You should not use this package yet, as it is poorly documented and is missing many important features

and the use of them causes more issues than the gain is. But, on the other hand, if Bootstrap is used - whose crispy-forms work fine - then there are
some clashes between Bootstrap and Bulma in the code.

So, to continue to use Bulma, the project does not use crispy-forms.

There was a failed attempt to use Bulma pageloader extension, so the npm install used in connection to that migth not be needed.

The plus and minus buttons that alter the quantity of an item going to the bag are set to be "faded" when disabled, i.e. when they reach the end
of their respective ranges. When a Bulma grey dark color is chosen for the buttons, in consitency with the rest of the site's pallette, the disabled button
gets "greyed" to the point where it's respective minus or plus sign only becomes distinguishable to the user when hovering over it.
Wheter this aids to the "intuitivenes" of the site, or is a hinderance to the user's comprehension, remains debatable.

There is an issue with the sort-selector - which sorts the products by a selected available option (A-Z, by price, by author, etc.) via a dropdown menu - the specific code
used (the templating language) in the `<option>` elements of the sort-selector, makes Bulma "not recognize" where the sort-select box "ends" when is rendered on the page,
so the down-arrow for the dropdown menu isn't displayed in the sort-select box, but rather at the far right of the page (that's the blue "chevron-down" icon that can be seen on
the far right, in level with the sort-select box).

There seems to be a weird thing going on with the `<tfoot>` element - the Bulma table footer.
The base structure of the table used was taken from Bulma's website, and the table footer should display at the bottom of the table.
But it does not - it's contents are rather rendered at the top of the table, above the table header. And when checked in the inspector in Chrome,
the table footer element seems completely empty (void of any content whasoever), and the .tfoot div with the actual contents shows in the inspector to
be above the `<table>` itself, but still within the .table-container div. Which is not the case in the actual html code.
This is why the "bag breakdown" (items cost, delivery cost, bag total) is displayed where it is in the bar view. This actual rendering works, but is completely unintentional
originally, and I seem to have no control over it.

There is space left on the product_detail page (i.e., when the product's image is displayed, the layout is as is, with space
to the right) because that was space planned for a product description - a short passage about the book taken from Amazon ("language" is to be scrapped
in the models for instance, and "description" is to be used instead).

#### **_Deployment_**

##### **_Local Deployment_**


In order to run this project locally, you will need to have installed: 
- An IDE of your choice (VS Code, etc.)
- [Python3](https://www.python.org/downloads/)
- [PIP](https://pip.pypa.io/en/stable/installing/) - to install the app's requirements (listed in the "requirements.txt")
- [GIT](https://www.atlassian.com/git/tutorials/install-git) - for version control

You would also require a [Stripe](https://www.stripe.com/) setup, to access the full intended functionality.

After this is installed, download the .ZIP file of the repository, unzip this file, and then:

- in the CLI with GIT installed, enter the following command: 
   
        git clone https://github.com/anteCedens/CI-MS3-cookbook.git

- navigate to the to path using the `cd` command. 
- create an `env` file with your credentials (values):
    - **os.environ["SECRET_KEY"]** >> This is a Django secret key; one is generated when you install Django; you can (and should)
    always get a new one at https://miniwebtool.com/django-secret-key-generator/ 
    - **os.environ["STRIPE_PUBLIC_KEY"]** >> you obtain this from Stripe
    - **os.environ["STRIPE_SECRET_KEY"]** >> you obtain this from Stripe 
- install all of the app's requirements for running, listed in the requirements.txt file, by using the following command:
    
        pip3 install -r requirements.txt

- migrate your models (effectively create a database) using:

        python3 manage.py migrate

- create a superuser using: 

        python3 manage.py createsuperuser 
- now you should then be able to launch your app using the following command in your terminal:

        python3 manage.py runserver

##### **_Remote Deployment_**

To remotely run this project: 

- in your GitPod workspace, create a `requirements.txt` file using this command in the terminal: `pip3 freeze > requirements.txt`.
- create a `Procfile` using this command in the terminal: `echo web: python app.py > Procfile`.
- set up your `Procfile` like so: web: `gunicorn [your_Django_project_name].wsgi:application`
- `git add` and `git commit` the new requirements and Procfile and then `git push` the project to GitHub.
- go to [Heroku](https://dashboard.heroku.com/login)
- click the "new" button, give the project a name & set the region to Europe. 
- from the Heroku dashboard of your newly created application, click on "Deploy" > "Deployment method" and select GitHub.
- confirm the linking of the heroku app to the correct GitHub repository.
- in the Heroku dashboard for the application, click on "Settings" > "Reveal Config Vars".
- set the config variables as so:

| Key | Value | 
    --- | --- 
    AWS_ACCESS_KEY_ID | `<secret key>` | 
    AWS_SECRET_ACCESS_KEY | `<secret key>` |
    AWS_STORAGE_BUCKET_NAME | `<AWS S3 bucket name>` |
    DATABASE_URL | `<your postgres database url>` |
    SECRET_KEY | `<django secret key>` |
    STRIPE_PUBLIC_KEY | `<stripe public key>` |
    STRIPE_SECRET_KEY | `<stripe secret key>` |
    USE_AWS | `True` |

You get your Postgres database url from Heroku.

- then back in the terminal in GitPod
    - enter the heroku Postgres shell
    - migrate the database models again, as described above (this is to create the database now in Postgres)
    - create your superuser account again, as described above (this is to create the superuser now in Postgres)

- in the Heroku dashboard, click "Deploy" (>> "Manual Deploy" >> master branch >> "Deploy Branch")
- the application should now be deployed (after you wait a bit for the build to be completed)


## **Credits**

### **Content**

Info about the books (title, author, publisher, rating, etc.) is taken from Amazon, but needn't represent those actuall
details on Amazon (especially in regards to rating and price).

### **Media**

Background image: 
- https://weheartit.com/entry/161231357

Site logo/favicon:
- https://www.clipartmax.com/middle/m2i8A0G6b1K9b1i8_open-book-design-book-open-vector-png-and-vector-open-book-logo/

Product images are all from https://www.amazon.co.uk/. Their urls are contained in the code.

Icons used are from:
- https://fontawesome.com/

### **Acknowledgements**

Chief dependencies are referenced in the code and/or mentioned already above:

The project in general tries to emulate Code Institute's tutorial project:

- https://github.com/ckz8780/boutique_ado_v1

Beating heart animation modified from:

- https://www.freecodecamp.org/learn/responsive-web-design/applied-visual-design/make-a-css-heartbeat-using-an-infinite-animation-count

Add-to-bag animation modified from:

- https://codepen.io/designcouch/pen/OJPdZxg (author: Jesse Couch)

Back-to-top button modified from:

- https://www.w3schools.com/howto/howto_js_scroll_to_top.asp

As writing the readme.md goes, for me, since project one, when in doubt or stuck, it's always been W.W.C.L.D.: 
What Would Claire Lally Do?:

- https://github.com/ClaireLally8

Other resources used:

- https://encycolorpedia.com/
- https://www.diffchecker.com/diff
- https://encycolorpedia.com/
- https://hnet.com/png-to-ico/