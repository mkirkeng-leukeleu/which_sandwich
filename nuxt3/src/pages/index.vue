<template>
  <NuxtLayout>
    <div class="container">
      <h1>Hello, {{ getUsername }}. Where to?</h1>
      <ul>
        <NuxtLink to="/order"><li>๐งพ Order</li></NuxtLink>
        <NuxtLink to="/orderHistory"><li>๐ Order history</li></NuxtLink>
        <NuxtLink to="/sandwiches"><li>๐ฅช Sandwiches</li></NuxtLink>
        <NuxtLink to="/about"><li>๐ About</li></NuxtLink>
        <NuxtLink to="/logout"><li>๐ Log out</li></NuxtLink>
      </ul>
    </div>
  </NuxtLayout>
</template>

<script>
export default {
  setup() {
    definePageMeta({
      middleware: "require-auth"
    })
  },
  computed: {
    getUsername() { return localStorage.getItem("username") }
  }
}
</script>

<style scoped>
ul {
  list-style: none;
}

li {
  padding: .25rem;
}
</style>
