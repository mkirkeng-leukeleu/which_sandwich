// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  srcDir: 'src/',
  ssr: false,
  app: {
    rootId: 'app'
  },
  modules: [
    '@nuxt/content'
  ]
})
