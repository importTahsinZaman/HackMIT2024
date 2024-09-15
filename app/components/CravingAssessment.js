import { Text, View } from "react-native";
import { LineChart } from "react-native-gifted-charts";

export default function CravingAssessment({ data }) {
  return (
    <View className="p-2 bg-[#648aff] shadow rounded-2xl h-[47%] w-[92%] flex flex-row items-center justify-evenly">
      <View className="flex items-center w-[45%]">
        <Text className="text-3xl font-semibold text-white">Craving:</Text>
        <Text className="text-3xl font-semibold text-white">
          {data > 0 ? data : 0}%
        </Text>
      </View>
      <View className="w-[45%] text-center items-center justify-center">
        <View className="w-30%">
          <Text className="text-3xl font-semibold text-white text-center items-center justify-center">
            {data <= 50 && "Looking good!"}
            {50 < data && "Harmonic will take care of it!"}
          </Text>
        </View>
      </View>
    </View>
  );
}
