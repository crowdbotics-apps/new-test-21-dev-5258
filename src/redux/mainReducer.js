import { combineReducers } from "redux";

/**
 * You can import more reducers here
 */


//@BlueprintReduxImportInsertion
import EmailAuth59349Reducer from '../features/EmailAuth59349/redux/reducers';
import CalendarView47325Reducer from '../features/CalendarView47325/redux/reducers';
import EmailAuthReducer from '../features/EmailAuth/redux/reducers';

export const combinedReducers = combineReducers({
  blank: (state, action) => {
    if (state == null) state = [];
    return state;
  },


  //@BlueprintReduxCombineInsertion
EmailAuth59349: EmailAuth59349Reducer,
CalendarView47325: CalendarView47325Reducer,
EmailAuth: EmailAuthReducer,

});