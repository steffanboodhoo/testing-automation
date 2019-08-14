import {types} from './actions';

const initialState = {
    user:'steffan boodhoo'
}

export default (state = initialState, action) => {
    switch(action.type){
        case(types.TEST):
            return {...state}
        default:
            return {...state}

    }
}