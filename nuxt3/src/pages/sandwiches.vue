<template>
  <NuxtLayout>
    <div >
      <NuxtLink 
        class="sandwich"
        v-for="sandwich in sandwiches"
        :to="'sandwich/' + sandwich.meta.slug"
      >
        <img v-if="sandwich?.image" :src="getImageUrl(sandwich)" :alt="sandwich.image.title">
        <div class="description">
          <h1>{{ sandwich.name }}</h1>
          <p>{{ sandwich.short_description }}</p>
        </div>
      </NuxtLink>
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
      sandwiches: [],
    }
  },
  created() {
    this.getSandwichList();
  },
  methods: {
    getSandwichList() {
      fetch(
        this.appConfig.SANDWICHES_URL + '/pages/?type=sandwiches.sandwich&fields=_,id,slug,name,image,short_description'
      ).then(res => res.json())
      .then(json => this.sandwiches = json.items)
    },
    getImageUrl(sandwich) {
      return this.appConfig.SANDWICHES_URL + sandwich?.image?.url
    }
  }
}
</script>

<style scoped>
.sandwich {
  display: grid;
  grid-template-columns: 1fr 1fr;
  margin-bottom: 1rem;
}

.description {
  margin-left: 1rem;
}

img {
  max-height: 8rem;
  width: 100%;
  object-fit: cover;
  border-radius: 2%;
}

p {
  color: var(--color-text);
}
</style>
