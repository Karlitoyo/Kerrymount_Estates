**Kerrymount Estates** - ***ReadMe***


Kerrymount-Estates is designed at its core to be simplistic and user friendly with the capability to access real time property prices and locations for available properties
advertised on the site. Users can access the website, sign-up / login to the service to book a property.

The website development and purpose has been broken down into the detailed sections below -

  > ## Contents


* [Features](https://github.com/Karlitoyo/Kerrymount_Estates#UX)
    - [Users](https://github.com/Karlitoyo/Kerrymount_Estates#Users)
    - [Strategy](https://github.com/Karlitoyo/Kerrymount_Estates#Strategy)
    - [Scope](https://github.com/Karlitoyo/Kerrymount_Estates#Scope)
    - [Structure](https://github.com/Karlitoyo/Kerrymount_Estates#Structure)
 * [Skeleton](https://github.com/Karlitoyo/Kerrymount_Estates#Skeleton)
    - [Wireframes](https://github.com/Karlitoyo/Kerrymount_Estates#Wireframes)
    - [Surface](https://github.com/Karlitoyo/Kerrymount_Estates#Surface)
 * [Development](https://github.com/Karlitoyo/Kerrymount_Estates#Development)
    - [Current-Features](https://github.com/Karlitoyo/Kerrymount_Estates#Current-Features)
    - [Further-Development](https://github.com/Karlitoyo/Kerrymount_Estates#Further-Development)
 * [Technologies-Utilised](https://github.com/Karlitoyo/Kerrymount_Estates#Technologies-Utilised)
 * [Testing](https://github.com/Karlitoyo/Kerrymount_Estates#Testing)
 * [Deployment](https://github.com/Karlitoyo/Kerrymount_Estates#Deployment)
    - [Deployed-Site](https://github.com/Karlitoyo/Kerrymount_Estates#Deployed-Site)
    - [Walkthrough](https://github.com/Karlitoyo/Kerrymount_Estates#Walkthrough)
 * [User-Stories](https://github.com/Karlitoyo/Kerrymount_Estates#User-Stories)
 * [Credits](https://github.com/Karlitoyo/Kerrymount_Estates#Credits/Media)
 * [Creators](https://github.com/Karlitoyo/Kerrymount_Estates#Creators)


  > # UX

The UX has been designed to be easy to navigate with the Navigation bar on the top of the page across all pages of the site. The Home page provides information on the business itself
such as licences held and contact information. A search function is provided in the first section of the home page which allows users to search for individual properties within the sites database.
The User can then login or register for the site using either email login or social media login. Upon logging in the user is then available to search the seperate sections of the site
rental properties or sale properties. Upon selecting a property to purchase the user can then add the selected property to their wallet and proceed to the checkout page for review of the
purchase information. Upon the user being satisfied with their purchase they then proceed to the checkout page and complee the checkout form and sumbit payment information to completed
the purchase.

## Users

The website has a target audience of 18-60 year olds searching for properties within a specific area or location. Users can have the option of searching the database of properties
or logging into the application to make purchase or rent a property.

## Strategy

The stratgey for the website is to attract users to view available properties. The website makes use of Materialize css for a polished finish and responsive layout.
Making use of Postgres db with Heroku to store user logins and also through making use of social media icon for google login. This is to encourage users to store their
information and provide weekly updates. Auto emails have been set up to allow for emails to be sent directly from django.

## Scope

The scope of the project is to allow users to purchase properties or rent a property from the site directly rather than visiting an estate agent or auctioneers.


## Structure

**Kerrymount-Estates Home**

The home page provides users with the initial landing page and is designed to be entice and encourage users to delve 
deeper into the service. The home page provides details on the service offering and promotional content.

**For Rent**

The rental page allows users to view the available rental properties on the site and to book a specific property.

**For Sale**

The sale page allows a user to view the available properties for sale on the site.

**All Propertys**

The all Propertys page provides a full listing of all the properties on the site and allows users to select a given property and add to their Wallet.

**Wallet**

The Wallet allows users to add specific propertys they are interested in and to progress to checkout. The wallet will hold the chosen property while the user navigates the
website and shows a total amount of the property cost on the navigation bar.


> # Skeleton

Wireframes for the main navigation pages can be found below -

 ## Wireframes
 
- [Homepage](https://github.com/Karlitoyo/Zapit/blob/master/Wireframes/Login.png)
- [Inputs](https://github.com/Karlitoyo/Zapit/blob/master/Wireframes/Inputs-Page.png)
- [Bank-Authentication](https://github.com/Karlitoyo/Zapit/blob/master/Wireframes/Bank-Authentication.png)
- [Dashboard](https://github.com/Karlitoyo/Zapit/blob/master/Wireframes/Dashboard.png)
- [Forecast](https://github.com/Karlitoyo/Zapit/blob/master/Wireframes/Forecast.png)
- [Results](https://github.com/Karlitoyo/Zapit/blob/master/Wireframes/Results-Page.png)


## Surface

The surface of the site is designed to be eye catching and make use of responsive UI which materilize css provides. The django web framework provides a powerful admin portal for
easily updating the database of available properties. The structure is layed out to be both user friendly with ease of navigation on both mobile and web.


 > # Development

 ## Current-Features

Current features consist of the search function which is available to users who have both signed up to the site and for users who may wish to browse the available number
of properties on the database. Should a user decide to create an account they can sign up using their email and user name or alternatively can make use of the social media
'Google' login function for easy registration. Auto email confirmation is also set up for this process. Users can add specific projects to their wallet and then progress to 
checkout with the items in their wallets.

## Further-Development

Further development of the site can include an auction calculator or bidding system in which users can place bids on specific properties. This would draw more users to the site and
allow 

## Technologies-Utilised

- HTML
- CSS
- [Java-script](https://www.javascript.com/)
- [Materialize](https://materializecss.com/)
- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Postgres](https://www.postgresql.org/)
- [Heroku](www.heroku.com)


- [Google Fonts](https://fonts.google.com/)
- [HTML Validator](https://validator.w3.org/)
- [CSS Validator](https://validator.w3.org/)

> # Deployment

## Deployed-Site

**Kerrymount-Estates -** (https://kerrymount-estates.herokuapp.com/)

## Walkthrough
 1. User visit's site, enters information on MyInformation page (name, address, bank a/c information, approval to connect via PSD2)(***submit disabled for demonstration***).
 2. User then visits cashflow page and inputs salary, savings, amount of debt + relevant outgoings. 
 3. Response is then given based on total disposable income. 
 4. User is then presented with results page where user spending is graphed and suggested reductions are provided.

The site is deployed on Heroku and code is available to view using Github.
Navigated to Github account, on the top left of the screen select "Zapit" repository, 
Env.py holds relevant mongo db address + password, IP and PORT and secret key.
A number of dependencies are required to run the system, flask, flask_pymongo, dnspython which are
outlined in the requirements.txt file.

- Zapit : (https://github.com/Karlitoyo/Zapit)

**Cloning**

Can be achieved by selecting the green highlighted button which states - "Clone or Download" via the webpage: (https://github.com/Karlitoyo/Zapit) this will 
give the option of downloading a .zip file or opening in desktop an option to clone using HTTP is also given for cloning and running project locally through Gitpod. 
Make use of the git pull function (if required to update the branch), git clone and git push to named repository.

**Version-Control**

All versions of the system are based around a calculator and input model for cashflow and balance sheet. Version 0.2 will include login functionality and user profile which will allow for
live data being stored on database and then visualised on results.html page. Proceeding versions will allow for PSD2
connectivity and full API integration.

> # User-Stories

## First case example user experience

Middle income user who has difficulty meeting loan obligations and struggles with regular savings -

Upon entering the site user will be taken to the home page. Upon visiting the home page the user will then visit the
MyInformation page and input relevant requested user information. Name, Surname, Address, DOB, Gender, Country of Residence,
E-Mail. The user will then visit the 'Bank Reference' section and provide a reference that was emailed securely to the user
upon providing their email in the previous section. The user will have provided the relevant required information securely
to connect their bank account to our service, the user will then input their annual salary + desired savings.
The user will need to select the 'connect to Zapit tickbox' which will then connect to the users bank account under PSD2.
Any additional information will then be put into the additional information page ie bank account information if required
or copy of passport / driver's licence. The user will then be connected to Zapit and payments can be managed through the site.
The 'MyFinances' page outlines the simplicity of the service. A user will be presented with an amount and will select from the 
available emoji's which best describes the amount spent. This removes mental barrier a user has around their finances being 
numbers and something that is alien to them. It creates a more comfortable environment in which to manage their savings. The 
results page then provides further breakdown of user spending and graphs how they spent and provides methods by which to
save.

## Second case example user experience

Low income user who is in arrears on mortgage and cannot maintain current levels of debt to salary -

User visits site. Provides full requested information as required for assessment to commence. Further assessment is
required to understand level of debt of user to meet desired savings figure. User connects via PSD2 and consents for 
transactions to be assessed to manage finances. Based on user spending assessment can identify reductions in weekly shopping
and recommend specific items which can provide savings. System recognises reductions available on heating and electricity 
further reductions in TV/Broadband. User can now meet contractual mortgage repayments due to reductions suggested. Bank can
restructure loan in line with customer improved affordability.


## Developer comments

Zapit will continue to develop to include live data for testing purposes. The Zapit web application will migrate to the Django web framework.
This will improve time to market and ensure testing of further development for planned functionality with allauth 
for login through google and social media. While the web based application is mobile ready further reach can be achived through Google play 
store and Apple App Store.


> # Credits

Special thanks must be given to the creators of all the above-mentioned sources and technologies that were used to develop Zapit.

> # Creators

- Karl Timmins
- Jacob George