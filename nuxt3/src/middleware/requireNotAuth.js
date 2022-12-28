export default defineNuxtRouteMiddleware((to, from) => {
  if (localStorage.getItem('API_token')) {
    return navigateTo("/")
  }
});
