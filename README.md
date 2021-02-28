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
This will aid to reduce costs for user and in a time when alot of proactices are going digital further online property sales will increase as a result.


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
 
 My wireframes Subscription has unfortunately lapsed


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
allow for further revenue to be generated through commissions. 

## Technologies-Utilised

- HTML
- CSS
- [Java-script](https://www.javascript.com/)
- [Materialize](https://materializecss.com/)
- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Postgres](https://www.postgresql.org/)
- [Heroku](www.heroku.com)
- [Stripe](www.stripe.com)


- [Google Fonts](https://fonts.google.com/)
- [HTML Validator](https://validator.w3.org/)
- [CSS Validator](https://validator.w3.org/)

> # Deployment

## Deployed-Site

**Kerrymount-Estates -** (https://kerrymount-estates.herokuapp.com/)

## Walkthrough
 1. User visit's site, User can sign up to login / register or alternatively browse using the search function on home page.
 2. User signs up or logins into the site using the main navigation bar.
 3. User browses categories of produucts for rent of for sale or all products.
 4. User selects desired product for purchase or rental and proceeds to add the item to their wallet.
 5. User then proceeds to chackout and confirms order securely with payment via stripe.

The site is deployed on Heroku and code is available to view using Github.
Navigated to Github account, on the top left of the screen select "Kerrymount_Estates" repository, 
All enviorment variables are stored on Heroku so user will require individual variables for db or stripe API.
A number of dependencies are required to run the system, django, stripe, Pillow, oauthlib, gunicorn, Flask,psycopg2-binary, boto3 among others which are
outlined in the requirements.txt file.

- Kerrymount-Estates : (https://github.com/Karlitoyo/Kerrymount_Estates)

**Cloning**

Can be achieved by selecting the green highlighted button which states - "Clone or Download" via the webpage: (https://github.com/Karlitoyo/Kerrymount_Estates) this will 
give the option of downloading a .zip file or opening in desktop an option to clone using HTTP is also given for cloning and running project locally through Gitpod. 
Make use of the git pull function (if required to update the branch), git clone and git push to named repository.

**Version-Control**

Differing Versions of this project have been developed. Initially the website had a rental and property section. An all proerties section was then added to include both rental and 
for sale properties. Further version included a wallet to store a users selected property. Next version upon review required was the checkout application as a user was then required to
make purchase of their chosen property. Stripe was then integrated to accomplish this function. Social media login was also a feature that was brought in later to the project. Search 
function was integrated to include searching from the homepage. This caused an issue as it allowed for unauthroised (non-registered users) to progress to the checkout without signing in.
An if statements within the hmtl fixed this issue. Resolved a number of issues with stripe payments integration as for final stages of project. Mainly related to form submission and 
sucessful re-direct.

> # User-Stories

## First case example user experience

Couple who wish to purchase property for the first time.

Users wishes to purchase property in given location. Users visit site and search database for property in location 'Blackrock'. Users are shown available properties in Blackrock with
photo and description of property. Users then login to site to progress with purchase scurely. Users visit viewed property details, details include price, rating, and a description of the product and image. Users then revert to homepage and search for alternative property in
'Sandyford. Users are happy with the price and description and adds the property to their wallet. Users then continue browsing the site. Users decide to checkout product from wallet
and selects checkout. Users then enter payment information and secure property purchase.

## Second case example user experience

Single male wishing to rent property in Ireland

User visits site and commences search for rental property in City Center. User is provided with a selection of properties from the database. User creates account using social media
login function and enters the rent section of the website. Upon user reviewing the rental properties available the user selects a city center location property within their price range.
The user reads the description and follows the link provided to the all properties page. The user adds the property to their wallet and proceeds to the checkout section. The user 
enters their information and checks out securely with stripe.


## Developer comments

For my milestone project I initially has a seperate project which I was working on using flask creating income calculator. My inital intention was to port this application over to Django and continue to develop
it through Django. I am currently stil developing this product however it would not meet all the requirements of the milestone project integration of payments etc. I then decided to
create this mobile web properties site for a family member who requires an online presense. I will continue to develop. I had difficulty with the json data initally as I amended the 
data provided in the course to fit my need. This caused some issues with connecting the rent / sale page to the product id's as they are not working off of the same data. As can be 
seen in my sale.html + rent.html these properties are rendered using html whereas the all propertys page can itereate through the data uploaded to django.

> # Credits

Special thanks must be given to the creators of all the above-mentioned sources and technologies that were used to develop Zapit.

> # Creators

- Karl Timmins