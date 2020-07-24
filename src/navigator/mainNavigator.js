import { createAppContainer } from 'react-navigation';
import { createStackNavigator } from 'react-navigation-stack';
import {createDrawerNavigator} from 'react-navigation-drawer';

import SplashScreen from "../features/SplashScreen";
import SideMenu from './sideMenu';
//@BlueprintImportInsertion
import EmailAuth59349Navigator from '../features/EmailAuth59349/navigator';
import CalendarView47325Navigator from '../features/CalendarView47325/navigator';
import BlankScreen5487Navigator from '../features/BlankScreen5487/navigator';
import BlankScreen5485Navigator from '../features/BlankScreen5485/navigator';
import EmailAuthNavigator from '../features/EmailAuth/navigator';

/**
 * new navigators can be imported here
 */

const AppNavigator = {
    SplashScreen: {
      screen: SplashScreen
    },
    //@BlueprintNavigationInsertion
EmailAuth59349: { screen: EmailAuth59349Navigator },
CalendarView47325: { screen: CalendarView47325Navigator },
BlankScreen5487: { screen: BlankScreen5487Navigator },
BlankScreen5485: { screen: BlankScreen5485Navigator },
EmailAuth: { screen: EmailAuthNavigator },

    /** new navigators can be added here */
};

const DrawerAppNavigator = createDrawerNavigator(
  {
    ...AppNavigator,
  },
  {
    contentComponent: SideMenu,
    initialRouteName: 'SplashScreen',
  },
);

const AppContainer = createAppContainer(DrawerAppNavigator);

export default AppContainer;
