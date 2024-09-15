import { StatusBar } from "expo-status-bar";
import React, { useState, useEffect } from "react";
import { SafeAreaView, Text, View } from "react-native";
import CurrentNicLevel from "../components/CurrentNicLevel";
import DaysRemaining from "../components/DaysRemaining";
import Progress from "../components/Progress";
import { supabase } from "../../lib/supabase";
import CravingAssessment from "../components/CravingAssessment";

export default function App() {
  const [data, setData] = useState();

  async function getData() {
    const { data, error } = await supabase
      .from("terra_current")
      .select("")
      .eq("id", "1");

    setData(data);
  }

  useEffect(() => {
    getData();
    setInterval(getData, 15000);
  }, []);

  if (data) {
    return (
      <SafeAreaView className="w-screen h-screen bg-gray-50">
        <Text className="ml-6 mt-4 text-3xl font-bold text-gray-500">
          Hi Tahsin! 👋
        </Text>
        <View className="flex-row mt-4 justify-evenly">
          <CurrentNicLevel data={data[0]["si_rate"]}></CurrentNicLevel>
          <DaysRemaining></DaysRemaining>
        </View>
        <View className="top-[-208] w-full justify-center items-center">
          <Progress></Progress>
        </View>
        <View className="top-[-404] w-full justify-center items-center">
          <CravingAssessment data={data[0]["stress"]}></CravingAssessment>
        </View>

        <StatusBar style="auto" />
      </SafeAreaView>
    );
  } else {
  }
}
