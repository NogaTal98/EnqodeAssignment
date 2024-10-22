<template>
  <v-container>
    <v-card class="mx-auto my-4" max-width="400">
      <v-card-title>{{ companyName }}</v-card-title>
      <v-card-subtitle>Zero-Trust Score: {{ zeroTrustScore }}</v-card-subtitle>

      <v-alert :type="riskCategoryType" outlined class="my-4">
        Risk Category: {{ riskCategory }}
      </v-alert>

      <v-card-text>
        <div v-for="(value, key) in metrics" :key="key">
          <p>{{ key }}: {{ value.score }}</p>
          <v-progress-linear
            v-model="value.score"
            color="primary"
            height="10"
            striped
          ></v-progress-linear>
          <small>{{ value.description }}</small>
        </div>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script>
  export default {
    name: 'ZeroTrustWidget',
    data() {
      return {
        companyName: 'FinTechSecure Ltd.',
        zeroTrustScore: 58.5,
        riskCategory: 'Moderate Risk',
        metrics: {
          'Network Security': {
            score: 70,
            description: 'Network secure with strong encryption.',
          },
          'User Authentication': {
            score: 50,
            description: 'Authentication practices need improvement.',
          },
          'Data Encryption': {
            score: 65,
            description: 'Sensitive data encryption in place.',
          },
          'Device Management': {
            score: 40,
            description: 'Device management policies are lacking.',
          },
        },
      }
    },
    computed: {
      riskCategoryType() {
        switch (this.riskCategory) {
          case 'Low Risk':
            return 'success'
          case 'Moderate Risk':
            return 'warning'
          case 'High Risk':
            return 'error'
          default:
            return 'info'
        }
      },
    },
  }
</script>
