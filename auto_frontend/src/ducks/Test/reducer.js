import { types } from './actions';
let initial_state = {
    load_more: true,
    tests: []
}

export default (state = initial_state, action) => {
    switch (action.type) {
        case (types.RECEIVE_TESTS): {
            return {
                ...state,
                tests: state.tests.concat(action.payload.tests)
            };
        }
        default:
            return { ...state };
    }
}