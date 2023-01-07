<template>
  <NuxtLayout>
    <div class="container">
      <img v-if="sandwich?.image" :src="getImageUrl" :alt="sandwich.image.title">
      <h1 class="green">
        {{ sandwich.name }}
        {{ sandwich.vegetarian ? '🥦' : '' }}
      </h1>
      <p>{{ sandwich.short_description }}</p>
      <br />
      <div v-html="sandwich.long_description"></div>
    </div>
  </NuxtLayout>
</template>

<script>
export default {
  setup() {
    const appConfig = useAppConfig();
    return { appConfig }
  },
  data() {
    return {
      sandwich: {}
    }
  },
  mounted() {
    this.getSandwichPage()
  },
  methods: {
    getSandwichPage() {
      fetch(
        this.appConfig.API_URL + "/sandwiches/pages/find/?html_path=" +
        this.$route.params.slug
      ).then(res => res.json())
      .then(json => this.sandwich = json)
    }
  },
  computed: {
    getImageUrl() {
      return this.appConfig.API_URL + this.sandwich?.image?.meta.download_url
    }
  }
}
</script>

<style scoped>
img {
  height: 10rem;
  width: 100%;
  object-fit: cover;
  margin-bottom: .5rem;
  border-radius: 2%;
}
</style>
