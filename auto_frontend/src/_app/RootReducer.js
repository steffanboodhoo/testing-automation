import {combineReducers} from 'redux';
import App from '../ducks/App/reducer';
import Test from '../ducks/Test/reducer';

const RootReducer = combineReducers({
    App,
    Test
});

export default RootReducer;