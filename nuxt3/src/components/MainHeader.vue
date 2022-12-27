<template>
  <div class="header">
    <img
      alt="Big sandwich"
      class="logo"
      src="../assets/sandwich.svg"
      width="125"
      height="125"
    />

    <div class="wrapper">
      <div class="greetings">
        <h1 class="green">{{ title }}</h1>
        <h3>{{ subtitle }}</h3>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    title: {
      type: String,
      default: "Which Sandwich?"
    },
    subtitle: {
      type: String,
      default: "Time to choose!"
    }
  }
}
</script>

<style scoped>
.logo {
  display: block;
  margin: 0 auto 2rem;
}

h1 {
  font-weight: 500;
  font-size: 2.6rem;
  top: -10px;
}

h3 {
  font-size: 1.2rem;
}

.greetings h1,
.greetings h3 {
  text-align: center;
}

@media (min-width: 1024px) {
  .header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
  .logo {
    margin: 0 2rem 0 0;
  }

  .greetings h1,
  .greetings h3 {
    text-align: left;
  }
}
</style>
