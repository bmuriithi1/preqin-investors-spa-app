<template>
    <h1>Preqin Investor Data</h1>
  
    <div class="card">
        <div v-if="investorInfoLoading"> 
            Loading Investor Data... 
        </div>
        <div v-else>            
            <DataTable v-model:selection="firm" :value="investorInfo" stripedRows selectionMode="single" tableStyle="min-width: 50rem">
                <Column field="firm_id" header="Firm ID"></Column>
                <Column field="firm_name" header="Firm Name"></Column>
                <Column field="firm_type" header="Firm Type"></Column>
                <Column field="date_added" header="Date Added"></Column>
                <Column field="address" header="Address"></Column>
            </DataTable>
            <p style="color:red"> 
                <strong>
                    Select a particular row to get commitment information for that firm 
                </strong> 
            </p>
        </div>
    </div>
</template>
  
<script>
import axios from 'axios'

export default {
    data() {
        return {
            investorIds: [2670, 2792, 332, 3611],
            investorInfo: null,
            investorInfoLoading: true,
            firm: null
        }
    },
    methods: {
        get_investor_data() {
            this.investorInfoLoading = true
            axios({
                url: `${import.meta.env.VITE_APP_API_SERVER}/investor-data/get-investor-data`,
                METHOD: "GET",
                params: {"investor_ids": this.investorIds.join(',')},
                headers: {"accept": "application/json"}
            })
            .then( response => {
                this.investorInfo = response.data
                this.investorInfoLoading = false
            })
            .catch( error => {
                console.log(error)
                if (error.response) {
                    console.log(error.response.status)
                }
                this.investorInfoLoading = false
            })
        },
    },
    watch: {
        firm: function() {
            // Update investorID in vuex store
            this.$store.commit("setInvestorId", this.firm.firm_id)

            // Navigate to investor page
            this.$router.push(`/investors/${this.$store.state.investorId}`)
        }
    },
    created() {
        this.get_investor_data()
    }

}

</script>

<style scoped>
</style>
  