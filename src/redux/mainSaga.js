import { all, takeEvery, take } from "redux-saga/effects";


//@BlueprintReduxSagaImportInsertion
import CalendarView47325Saga from '../features/CalendarView47325/redux/sagas';
import EmailAuthSaga from '../features/EmailAuth/redux/sagas';

function* helloSaga() {
  console.log("Hello from saga!");
}

export function* mainSaga() {
  yield all([
    takeEvery("TEST/ALO", helloSaga),
    // other sagas go here


    //@BlueprintReduxSagaMainInsertion
CalendarView47325Saga,
EmailAuthSaga,
    
  ]);
}