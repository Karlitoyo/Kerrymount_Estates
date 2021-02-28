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
information and provide weekly updates.

## Scope

The Scope of the service is to create financial literacy and encourage saving from a wider range of individuals.
This product can benefit individuals who rely on high interest loans or payday loans, this service can also benefit
current mortgage holders who are struggling to meet regular repayments or who may be in negative equity. This service
can also benefit individuals who are currently saving for a mortgage as the financial planning aspect of the service
will improve savings and can also be verified through the service.


## Structure

**Zapit Home**

The home page provides users with the initial landing page and is designed to be entice and encourage users to delve 
deeper into the service. The home page provides details on the service offering and promotional content.

**MyInformation**

The MyInformation page is required for a user's sign up **for the purpose of demonstration the MyInformation fields are not live.**
It was an option to include user registration and login through Werkzeug and store the logins via mongo, however for the 
purpose of demonstration this is not necessary. The user will input their name, address, email and other 
relevant information prior to commencing the service and provide consent to connect via PSD2. 
The user will then input their annual salary + desired savings amount.

**Cashflow**

The cashflow section allows for a user to calculate their disposable income on a yearly basis. The inputs are based
on most common user spends. The inputs are to be developed further to give a holistic view of a user's finances.
The results can be either positive or negative. A threshold of €10,000 has been set for disposable income which will
present a positive emoji if disposable income is above set threshold and a thinking emoji if below. Two separate text responses are
set for each outcome also depending on disposable income figure returned.

**MyFinances**

The MyFinances page is designed to be simple and user friendly. The emoji buttons will allocate 
a registered spend upon the user connecting via their bank account. The user will select the relevant spend and
this will track the spend within our database. The spends will be managed and then visually represented on the results page.

**Results**

The results page will graph a user's spending and provide a calculated saving based on their spending trends.
This can be expanded upon with live data received from users and also with the incorporation of our planned
voucher system in conjunction with local SME's. For purpose of demonstration the charts are not currently showing 
live data as inputs are not currently stored via mongo. Upon storing inputs graphs will visualise user's cashflow.


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

The surface of the website is intended to be easy to navigate and provide content that users find relevant to
their spending. The application is designed for minimal user interaction. An initial period of learning must
be undertaken before the system can recognise how a user's spending must be allocated and suggestions can be generated.
The navigation on mobile and desktop does not alter except for the navigation bar collapsing. The choice to use emoji's
as the primary method of identifying spending is backed up by data showing emoji use as becoming the new normal to communicate
within our target demographic as can be shown below - 

<p align="center">
    <img src= 'https://blog.emojipedia.org/content/images/2020/05/2-Emoji-Usage-on-Twitter-2.JPG'>
</p>

 > # Development

 ## Current-Features

Currently we have a system which can collect and store user data via Mongodb. We can collect and process user logins
and other relevant user data for sign up. This data can be used for locational purposes and for providing tailored
vouchers and spend recommendations. Upon successful API integration we can then begin to process user spend data and
begin to expand our current cash flow system based on further data points being received. Currently the MyFinances page
is a UI which is designed to be simplistic and encourage users to interact with the platform. The Cashflow page provides
a user to input their yearly Annual Salary + Total Savings. The user then inputs their total yearly debt + mortgage +
shopping + travel + childcare expenses and a figure for disposable income is provided. Further inputs can be included
and further analysis of spending upon user sign-up.


## Further-Development

Upon further development of the system we intend to incorporate Machine Learning capabilities within the back end expanded
balance sheet and cash flow system. Further to this accounting platform our voucher system can allow for targeted campaigns
based on local businesses within a user's area. This will not be invasive rather an aspect of the site users can visit
should they require a particular service. Blockchain is available and can lend itself to this service through the tokenisation
of vouchers which can be airdropped to a user or rewarded to a user for good spending/saving habits. IBM's open source 
blockchain fits purpose for integration with some modifications to the open source code. Further development will also include
a chat bot for 24hour customer queries, Machine Learning/AI for smart money management trends and real time spending and tracking.

***Digital Wallet (Zaps)***

The proposed voucher platform will include a digital wallet in which users can access their vouchers. This eco-system will be
connected to a user's smart-phone and included within the platform itself. Users can access their wallet to view their tailored
vouchers based on their spending. Partner businesses can target their audience based on user spending through the digital wallet
included with the service. Users can store their vouchers and spend as appropriate; vouchers can be dropped monthly / in line 
with a user's spending trends.

## Technologies-Utilised

- HTML
- CSS
- Java script
- [Bootstrap](https://getbootstrap.com/)
- [Python](https://www.python.org/)
- [MongoDB](https://www.mongodb.com/)
- [Heroku](www.heroku.com)


- [Google Fonts](https://fonts.google.com/)
- [HTML Validator](https://validator.w3.org/)
- [CSS Validator](https://validator.w3.org/)

> # Deployment

## Deployed-Site

**Zapit -** (https://kyc-aml-project-karl.herokuapp.com/)

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

> # Mobile-Application

- [Mobile Application Source Code](https://github.com/Karlitoyo/Zapit-Mobile-App)

Our Mobile Application is currently under development using Flutter and Dart programming language. We are in first stage development
currently with the UI being worked on. Currently Landing page, Home page, Cashflow Page, MyFinances page & Zaps mobile wallet page UI
in development with provided screenshot below. We intend to have a full UI built within the coming quarther which will include the features
as per our submission hosted via Heroku. We will then develop out the back end functions and API integration.
The Application will be available on IOS & Android and be available for download via both marketplaces upon completion.

***Mobile Application Progress Development Screenshots***

- [Landing Mobile Page](https://github.com/Karlitoyo/Zapit/blob/master/Wireframes/Zapit-Landing-App.png)
- [Home Mobile Page](https://github.com/Karlitoyo/Zapit/blob/master/Wireframes/Zapit-Home-App.png)
- [Cashflow Mobile Page](https://github.com/Karlitoyo/Zapit/blob/master/Wireframes/Zapit-Cashflow-App.png)
- [MyFinances Mobile Page](https://github.com/Karlitoyo/Zapit/blob/master/Wireframes/Zapit-MyFinances-App.png)
- [Zaps Wallet Mobile Page](https://github.com/Karlitoyo/Zapit/blob/master/Wireframes/Zaps-Wallet-App.png)

## Developer comments

Zapit will continue to develop to include live data for testing purposes. The Zapit web application will migrate to the Django web framework.
This will improve time to market and ensure testing of further development for planned functionality with allauth 
for login through google and social media. While the web based application is mobile ready further reach can be achived through Google play 
store and Apple App Store.

> # Business-Plan

## Timeframe

With the aid of development partners we can ensure smooth implementation of user connectivity, specifically 
implantation of PSD2 and planned site development for inclusion of voucher/business eco-system as outlined with
the revenue model. This can be achieved within a 6-8 month period for beta V1. Brand/product recognition will
be completed in conjunction with anticipated release of product launch.

**2 years to Irish market**
**4 years to European market**
**+4 global market**

## Costs

**Development**

We anticipate full development with inclusion of all above development features and time to market to cost circa €50,000 and 2 years to market.
Development team currently based in Ireland and South Africa. This gives two separate regions in which to go live. Both members have
past experience in project development and implementation which will aid in cost reductions to develop application successfully.

This cost can be further reduced through incubation development teams. This can allow for further cost allocation to
market the product.

**Marketing**

This will be targeted at our intended demographic age of 18-30 year olds and will be based on social media and relevant platforms initially.
As product/brand awareness improves further marketing management will be required to ensure market penetration is achieved. From research an
average social media marketing campaign can be achieved on €12,000 depending on budget.

## SWOT

- Strengths

Personal finances applications market is an increasing market. Recent analysis by Statista -
(https://www.statista.com/outlook/298/109/personal-finance/united-states)
indicates market growth to over €1 Billion in value by 2023 in the United States alone. A growth of 25%
from its current position.

The system has numerous strengths which include simple user-friendly UI making use of PSD2 for financial planning 
and enabling customers to take control of their finances. The simplicity of the system and the focus on the emoji 
language as the main method of interaction creates a UI that is friendly and provides simplistic and effortless 
management of user finances. We have identified that users will not wish to always interact with the application 
upon repeated spending this is achieved through sorting transactions and ensuring limited user interaction on 
spends through real time transaction monitoring.

- Weaknesses (Challenges)

Challenges identified predominantly relate to API integration specifically B2C. GDPR and ensuring strict management of consumer data is a priority and has been taken 
into consideration at all relevant stages of development.

- Opportunities

Opportunities lend itself to mortgage applications, term loan planning and individuals
who have difficulty in controlling their finances. The opportunities of the system also relate to local businesses who
can take advantage of the user base in their location and provide their service through the site based on our revenue model. 
User spending trends and data are collected and managed to provide valuable information on specific areas and spending
patterns.

- Threats

Threats relate to similar products. Mainly these relate to software for financial planners who in turn revert to clients
with the outcomes or provide subscription services as the main source of revenue. Zapit will automate this service and 
manage a user's spending and provide notifications on how well about user is at managing their spending. Specific software 
that provides a similar service would include Buxfer, Quicken, Mint, Emma.
Zapit will provide all of these services in one package with no subscription or added fees for extra functionality.

## Revenue Model

The revenue model will be based on data analytics predominantly predicting trends in user spending. Revenue will also
be derived from business partners who wish to promote their service through the application. The service being provided
without subscription will encourage users to save and suggests methods to do so. We can make use of partners' products
database to advertise cost reductions to users through the application.
All user data is currently stored on Mongodb which will migrate as requirements dictate. Currently this amounts to login data, 
once users are connected via PSD2 this data can be expanded to include spending data. Revenue will come from partner companies 
who wish to advertise services within the application eco-system. Zapit will provide targeted vouchers using niche marketing
to the correct audience making use of data analytics and specific demographics with click conversion as the primary model for charges.
This can be achieved through tokenisation of assets which can be dropped via further development of the platform. This is intended 
to be un-intrusive to the platform with users choosing to visit this area of the application should their needs require. 
Our service will be provided without a subscription aspect as this deters more uptake than it encourages to make use of the 
platform and intended eco-system. Our revenue model is geared towards data analytics and paid partnership with business/voucher platform.

<p align="center">
    <img src= 'https://lucid.app/publicSegments/view/f5d1f65b-6841-48c9-a79b-ce6cb73eb5d4/image.png'>
</p>

> # Credits

Special thanks must be given to the creators of all the above-mentioned sources and technologies that were used to develop Zapit.

> # Creators

- Karl Timmins
- Jacob George