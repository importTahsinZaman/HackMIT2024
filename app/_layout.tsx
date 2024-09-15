import { Stack } from "expo-router";

const RootLayout = () => {
  return (
    <Stack>
      <Stack.Screen
        name="(tabs)"
        options={{
          headerShown: false,
        }}
      />
      <Stack.Screen
        name="TestScreen"
        options={{
          headerTitle: "",
          headerBackTitle: "Home",
          headerStyle: {
            // backgroundColor: "#0000",
          },
        }}
      />
    </Stack>
  );
};

export default RootLayout;
