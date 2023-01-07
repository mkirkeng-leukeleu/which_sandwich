<template>
  <div class="container">
    <div>
      <p>
        <span class="green">Ordered on: </span>{{ orderData.order_date }}
      </p>
      <p>
        <span class="green">Email: </span>{{ orderData.email }}
      </p>
      <p>
        <span class="green">Sandwich: </span>
        <NuxtLink
          :to="'sandwich/' + orderData.sandwich.slug"
        >{{ orderData.sandwich.name }}</NuxtLink>
      </p>
      <p>
        <span class="green">Bread type: </span>{{ orderData.bread_type }}
      </p>
    </div>
  </div>
</template>

<script>
import sandwiches from '../sandwiches';

export default {
    props: {
      orderData: {
        type: Object
      }
    }
}
</script>

<style scoped>
.container {
  display: block;
  padding: 0.5rem;
}
</style>
