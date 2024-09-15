import { StatusBar } from "expo-status-bar";
import React from "react";
import { SafeAreaView, Text, View } from "react-native";

export default function History() {
  return (
    <SafeAreaView className="flex w-screen h-screen justify-center items-center">
      <Text>History!</Text>
      <StatusBar style="auto" />
    </SafeAreaView>
  );
}
