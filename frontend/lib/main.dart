"""
Parallel Flutter 應用入口
平行世界多智能體敘事系統的手機模擬器界面
"""
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

void main() {
  WidgetsFlutterBinding.ensureInitialized();
  SystemChrome.setPreferredOrientations([
    DeviceOrientation.portraitUp,
  ]);
  runApp(const ParallelApp());
}

class ParallelApp extends StatelessWidget {
  const ParallelApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Parallel — 平行世界',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
        useMaterial3: true,
      ),
      home: const HomeScreen(),
    );
  }
}

/// 首頁畫面，展示平行世界手機模擬器主界面
class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  int _currentIndex = 0;

  /// 頁面列表
  final List<Widget> _pages = const [
    SizedBox(child: Center(child: Text('消息'))),
    SizedBox(child: Center(child: Text('郵箱'))),
    SizedBox(child: Center(child: Text('劇情'))),
    SizedBox(child: Center(child: Text('設定'))),
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('平行世界'),
        elevation: 0,
      ),
      body: _pages[_currentIndex],
      bottomNavigationBar: NavigationBar(
        selectedIndex: _currentIndex,
        onDestinationSelected: (index) {
          setState(() => _currentIndex = index);
        },
        destinations: const [
          NavigationDestination(icon: Icon(Icons.chat), label: '消息'),
          NavigationDestination(icon: Icon(Icons.mail), label: '郵箱'),
          NavigationDestination(icon: Icon(Icons.auto_stories), label: '劇情'),
          NavigationDestination(icon: Icon(Icons.settings), label: '設定'),
        ],
      ),
    );
  }
}
