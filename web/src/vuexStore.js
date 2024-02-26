import { createStore } from 'vuex'

// Create vuex store
export const store = createStore({
    state: () => ({
        investorId: null
    }),
    mutations: {
        setInvestorId(state, id) {
            state.investorId = id
        }
    }
})