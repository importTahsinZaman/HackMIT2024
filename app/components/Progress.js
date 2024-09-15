import { Text, View } from "react-native";
import { LineChart } from "react-native-gifted-charts";

export default function Progress() {
  const data = [
    { value: 0.5 },
    { value: 0.4 },
    { value: 0.5 },
    { value: 0.5 },
    { value: 0.5 },
    { value: 0.7 },
    { value: 0.5 },
    { value: 0.5 },
  ];

  return (
    <View className="p-3 bg-white  shadow rounded-2xl h-[58%] w-[92%] flex items-center justify-center">
      <LineChart
        width={320}
        data={data}
        areaChart
        color1="#ff5c91"
        startFillColor1="#ff5c91"
        dataPointsColor1="#ff5c91"
        thickness1={4}
        xAxisThickness={0}
        yAxisThickness={0}
        dashWidth={1}
        yAxisTextStyle={{ color: "#4b5563", fontSize: 12 }}
        stepValue={0.07}
      />
      <Text className="text-gray-600">
        Nicotine Dosage History (Past 3 Hours)
      </Text>
    </View>
  );
}
