<template>
    <h1>Investor {{ this.$route.params.investor_id }} Commitment Info</h1>
  
    <div class="card">
        <!-- 
            <Dropdown v-model="assetClass" :options=assetClasses optionLabel="asset" placeholder="Select an Asset Class" class="dropdown w-full md:w-14rem" /> 
            For some reason the PrimeVue Dropdown component is glitchy. Investigate at some point as it looks nicer. Use HTML <select> for now.
        -->
        <label for="assetClasses" class ="dropdown center"> <strong> Select Asset Class: </strong></label> 
        <select name="assetClass" id="assetClass" class="dropdown center" @change="fetchCommitmentInfo()"> 
            <option value="pe"> pe </option> 
            <option value="pd"> pd </option> 
            <option value="re"> re </option> 
            <option value="inf"> inf </option> 
            <option value="nr"> nr </option> 
            <option value="hf"> hf </option> 
        </select>
        <div v-if="commitmentInfoLoading"> 
            <p> Loading Asset Data for {{ this.assetClass }} for investor {{ this.$store.state.investorId }}... </p>
        </div>
        <div v-else>
            <DataTable :value="commitmentInfo" stripedRows tableStyle="center min-width: 50rem">
                <Column field="asset_class" header="Asset Class"></Column>
                <Column field="currency" header="Currency"></Column>
                <Column field="amount" header="Commitment Amount"></Column>
            </DataTable>
        </div>
        <div>
            <p style="color:red"> 
                <strong>
                    Select asset class to get asset-specific information for investor {{ this.$route.params.investor_id }} 
                </strong> 
            </p>
        </div>
        <Button label='Home' @click="navigateHome" class="button" />
    </div>
</template>
  
<script>
import axios from 'axios'

export default {
    data() {
        return {
            assetClasses: ["pe", "pd", "re", "inf", "nr", "hf"],
            commitmentInfo: null,
            commitmentInfoLoading: false,
            assetClass: null,
        }
    },
    methods: {
        get_commitment_info(){
            this.commitmentInfoLoading = true
            axios({
                url: `${import.meta.env.VITE_APP_API_SERVER}/investor-data/get-investor-commitment-info/`,
                METHOD: "GET",
                params: {
                    "asset_class": this.assetClass,
                    "investor_id": this.$store.state.investorId
                },
                headers: {"accept": "application/json"}
            })
            .then( response => {
                this.commitmentInfo = response.data
                this.commitmentInfoLoading = false
            })
            .catch( error => {
                console.log(error)
                if (error.response) {
                    console.log(error.response.status)
                    this.commitmentInfoLoading = false
                }
            })
        },
        fetchCommitmentInfo() {
            this.assetClass = document.getElementById("assetClass").value;
            this.get_commitment_info()
        },
        navigateHome() {
            this.$router.replace(`/`)
        }
    },
    watch: {
        assetClass: function() {
            this.get_commitment_info()
        }
    },
}

</script>

<style scoped>
.button {
    background-color: #22c55e;
}
.dropdown {
    background-color: white;
    color: rgb(30, 3, 126);
    font-size: large;
    padding: 0.25em;
    margin-bottom: 0.5em;
}
.center {
    text-align: center;
}
</style>
  