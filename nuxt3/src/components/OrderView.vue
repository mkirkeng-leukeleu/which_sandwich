<template>
  <div class="container">
    <div>
      <p>
        <span class="green">Ordered for: </span>{{ formattedOrderDate }}
      </p>
      <p>
        <span class="green">Order created: </span>{{ orderData.created }}
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
  },
  computed: {
    formattedOrderDate() {
      const date = new Date(this.orderData.order_date);
      const options = {
        year: "numeric",
        weekday: "long",
        month: "short",
        day: "numeric",
      }

      return date.toLocaleDateString('nl-nl', options)
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
