
# <img src="./nuxt3/src/assets/sandwich.svg" width="50" height="50"> Which Sandwich
This is an exercise project for me to work with various technologies used at Leukeleu. It's a webapp which can be used to create and view the daily orders of sandwiches sent to a local sandwich shop.

# General structure
The frontend is completely separate from the backend and build using [Vue3](https://vuejs.org/) and [Nuxt3](https://nuxt.com/). It fetches all dynamic content from the backend API.
It can be deployed as a traditional SPA hosted using a NodeJS server, be rendered on the server using a NodeJS server or be pre-rendered at build time and hosted staticly using any web server.

The about page is created from a markdown file in this repository using a [Nuxt Content V2](https://content.nuxtjs.org/) while the sandwich pages are created from the Wagtail backend.

The backend uses Django and contains two applications:
 - 'api' for the orders which uses [Django rest framework](https://www.django-rest-framework.org/)
 - 'sandwiches' for the database of available sandwiches which uses headless [Wagtail](https://wagtail.org/) as CMS


# Known issues/TODOs
- The project does not use the file structure generally used by Leukeleu.
- ~~Core is not a very descriptive name for a django app.~~
