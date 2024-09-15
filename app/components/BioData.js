import { Pressable, Text, SafeAreaView, View } from "react-native";
import { Link } from "expo-router";

export default function BioData() {
  return (
    <View className="mb-4 mx-6  bg-white shadow rounded-2xl h-[28%] flex items-center justify-around flex-row">
      <View>
        <Text className="font-bold ">Stress:</Text>
        <Text>1a</Text>
      </View>
      <View>
        <Text className="font-bold">Sleep:</Text>
        <Text>2</Text>
      </View>
      <View>
        <Text className="font-bold">Heart Rate:</Text>
        <Text>3</Text>
      </View>
      {/* <View>
        <Text className="font-bold">Stress:</Text>
        <Text>3</Text>
      </View> */}
    </View>
  );
}
