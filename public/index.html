import React, { useState, useEffect, useMemo } from 'react';
import { 
  Calculator, 
  TrendingUp, 
  Users, 
  Settings, 
  Download, 
  Plus, 
  Trash2, 
  Save, 
  Wifi, 
  WifiOff,
  ChevronDown,
  ChevronUp,
  GraduationCap,
  Menu,
  X,
  BookOpen,
  PieChart
} from 'lucide-react';

// --- Constants & Utilities ---

const API_BASE_URL = "https://your-api-domain.com/api"; // Placeholder for user's API

// Official UAF Grading Tables
const GRADING_SCALES = {
  modern: [ // HEC / New Scheme (50% Pass)
    { min: 85, max: 100, gp: 4.00, grade: 'A' },
    { min: 80, max: 84.99, gp: 3.70, grade: 'A-' },
    { min: 75, max: 79.99, gp: 3.30, grade: 'B+' },
    { min: 70, max: 74.99, gp: 3.00, grade: 'B' },
    { min: 65, max: 69.99, gp: 2.70, grade: 'B-' },
    { min: 61, max: 64.99, gp: 2.30, grade: 'C+' },
    { min: 58, max: 60.99, gp: 2.00, grade: 'C' },
    { min: 55, max: 57.99, gp: 1.70, grade: 'C-' },
    { min: 50, max: 54.99, gp: 1.00, grade: 'D' },
    { min: 0, max: 49.99, gp: 0.00, grade: 'F' }
  ],
  legacy: [ // Old Scheme (40% Pass - Progressive)
    { min: 80, max: 100, gp: 4.00, grade: 'A' },
    { min: 65, max: 79, gp: 3.00, grade: 'B' }, // Often calculated progressively
    { min: 50, max: 64, gp: 2.00, grade: 'C' },
    { min: 40, max: 49, gp: 1.00, grade: 'D' },
    { min: 0, max: 39, gp: 0.00, grade: 'F' }
  ]
};

const calculateGP = (marks, totalMarks, scaleType = 'modern') => {
  if (!marks || !totalMarks) return 0;
  const percentage = (parseFloat(marks) / parseFloat(totalMarks)) * 100;
  const scale = GRADING_SCALES[scaleType] || GRADING_SCALES.modern;
  
  const gradeObj = scale.find(r => percentage >= r.min && percentage <= r.max);
  return gradeObj ? gradeObj.gp : 0;
};

const calculateGradeLetter = (marks, totalMarks, scaleType = 'modern') => {
  if (!marks || !totalMarks) return '-';
  const percentage = (parseFloat(marks) / parseFloat(totalMarks)) * 100;
  const scale = GRADING_SCALES[scaleType] || GRADING_SCALES.modern;
  const gradeObj = scale.find(r => percentage >= r.min && percentage <= r.max);
  return gradeObj ? gradeObj.grade : 'F';
};

const generateId = () => Math.random().toString(36).substr(2, 9);

// --- Components ---

const Header = ({ toggleSidebar, serverStatus }) => (
  <header className="bg-emerald-700 text-white shadow-lg sticky top-0 z-50">
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
      <div className="flex items-center space-x-3">
        <button onClick={toggleSidebar} className="lg:hidden p-2 rounded-md hover:bg-emerald-600 focus:outline-none">
          <Menu className="h-6 w-6" />
        </button>
        <div className="flex items-center space-x-2">
          <GraduationCap className="h-8 w-8 text-yellow-300" />
          <div>
            <h1 className="text-lg font-bold leading-tight">UAF Calculator</h1>
            <p className="text-xs text-emerald-200 hidden sm:block">University of Agriculture Faisalabad</p>
          </div>
        </div>
      </div>
      <div className="flex items-center space-x-4">
        <div className={`flex items-center space-x-1 px-3 py-1 rounded-full text-xs font-medium ${serverStatus ? 'bg-emerald-600 text-emerald-100' : 'bg-red-600 text-white'}`}>
          {serverStatus ? <Wifi className="h-3 w-3" /> : <WifiOff className="h-3 w-3" />}
          <span className="hidden sm:inline">{serverStatus ? 'Server Online' : 'Server Offline'}</span>
        </div>
      </div>
    </div>
  </header>
);

const Sidebar = ({ isOpen, activeTab, setActiveTab, closeSidebar }) => {
  const menuItems = [
    { id: 'calculator', label: 'CGPA Calculator', icon: Calculator },
    { id: 'forecast', label: 'Forecaster', icon: TrendingUp },
    { id: 'profiles', label: 'Profiles', icon: Users },
    { id: 'import', label: 'Import Result', icon: Download },
    { id: 'settings', label: 'Settings', icon: Settings },
  ];

  return (
    <>
      {/* Mobile Overlay */}
      {isOpen && (
        <div className="fixed inset-0 bg-black bg-opacity-50 z-40 lg:hidden" onClick={closeSidebar}></div>
      )}
      
      {/* Sidebar Content */}
      <aside className={`fixed lg:static inset-y-0 left-0 z-50 w-64 bg-white border-r border-gray-200 transform transition-transform duration-200 ease-in-out lg:transform-none ${isOpen ? 'translate-x-0' : '-translate-x-full'}`}>
        <div className="h-full flex flex-col">
          <div className="h-16 flex items-center px-6 border-b border-gray-100 lg:hidden">
             <span className="font-bold text-gray-800">Menu</span>
             <button onClick={closeSidebar} className="ml-auto p-2"><X className="h-5 w-5 text-gray-500" /></button>
          </div>
          <nav className="flex-1 py-6 px-3 space-y-1 overflow-y-auto">
            {menuItems.map((item) => (
              <button
                key={item.id}
                onClick={() => { setActiveTab(item.id); closeSidebar(); }}
                className={`w-full flex items-center space-x-3 px-4 py-3 rounded-lg text-sm font-medium transition-colors ${
                  activeTab === item.id 
                    ? 'bg-emerald-50 text-emerald-700' 
                    : 'text-gray-600 hover:bg-gray-50 hover:text-gray-900'
                }`}
              >
                <item.icon className={`h-5 w-5 ${activeTab === item.id ? 'text-emerald-600' : 'text-gray-400'}`} />
                <span>{item.label}</span>
              </button>
            ))}
          </nav>
          <div className="p-4 border-t border-gray-100">
            <div className="bg-emerald-900 rounded-xl p-4 text-center">
              <p className="text-xs text-emerald-200 mb-2">Developed for UAF Students</p>
              <div className="text-xs text-emerald-400 font-mono">v2.0.0 Stable</div>
            </div>
          </div>
        </div>
      </aside>
    </>
  );
};

const StatCard = ({ label, value, subtext, color = "emerald" }) => (
  <div className={`bg-white rounded-xl shadow-sm border border-gray-100 p-5 flex flex-col justify-between hover:shadow-md transition-shadow border-l-4 border-l-${color}-500`}>
    <p className="text-sm font-medium text-gray-500">{label}</p>
    <div>
      <h3 className={`text-2xl font-bold text-${color}-600 mt-1`}>{value}</h3>
      {subtext && <p className="text-xs text-gray-400 mt-1">{subtext}</p>}
    </div>
  </div>
);

// --- Main Views ---

const CalculatorView = ({ profile, updateProfile, settings }) => {
  const [expandedSemester, setExpandedSemester] = useState(null);

  const addSemester = () => {
    const newSem = {
      id: generateId(),
      name: `Semester ${profile.semesters.length + 1}`,
      subjects: [{ id: generateId(), name: 'Subject 1', marks: '', total: 60, ch: 3 }]
    };
    updateProfile({ ...profile, semesters: [...profile.semesters, newSem] });
    setExpandedSemester(newSem.id);
  };

  const removeSemester = (semId) => {
    if (window.confirm("Delete this semester?")) {
      updateProfile({ ...profile, semesters: profile.semesters.filter(s => s.id !== semId) });
    }
  };

  const updateSemester = (semId, newData) => {
    updateProfile({
      ...profile,
      semesters: profile.semesters.map(s => s.id === semId ? { ...s, ...newData } : s)
    });
  };

  const addSubject = (semId) => {
    const sem = profile.semesters.find(s => s.id === semId);
    const newSub = { id: generateId(), name: `Subject ${sem.subjects.length + 1}`, marks: '', total: 60, ch: 3 };
    updateSemester(semId, { subjects: [...sem.subjects, newSub] });
  };

  const updateSubject = (semId, subId, field, value) => {
    const sem = profile.semesters.find(s => s.id === semId);
    const updatedSubjects = sem.subjects.map(sub => 
      sub.id === subId ? { ...sub, [field]: value } : sub
    );
    updateSemester(semId, { subjects: updatedSubjects });
  };

  const removeSubject = (semId, subId) => {
    const sem = profile.semesters.find(s => s.id === semId);
    updateSemester(semId, { subjects: sem.subjects.filter(s => s.id !== subId) });
  };

  // Calculations
  const semesterStats = useMemo(() => {
    return profile.semesters.map(sem => {
      let totalQP = 0;
      let totalCH = 0;
      sem.subjects.forEach(sub => {
        const ch = parseFloat(sub.ch) || 0;
        const gp = calculateGP(sub.marks, sub.total, settings.gradingScale);
        totalQP += (gp * ch);
        totalCH += ch;
      });
      return { ...sem, gpa: totalCH ? (totalQP / totalCH).toFixed(2) : '0.00', totalCH };
    });
  }, [profile.semesters, settings.gradingScale]);

  const cgpaStats = useMemo(() => {
    let grandTotalQP = 0;
    let grandTotalCH = 0;
    profile.semesters.forEach(sem => {
       sem.subjects.forEach(sub => {
        const ch = parseFloat(sub.ch) || 0;
        const gp = calculateGP(sub.marks, sub.total, settings.gradingScale);
        grandTotalQP += (gp * ch);
        grandTotalCH += ch;
       });
    });
    return {
      cgpa: grandTotalCH ? (grandTotalQP / grandTotalCH).toFixed(2) : '0.00',
      totalCH: grandTotalCH
    };
  }, [profile.semesters, settings.gradingScale]);

  return (
    <div className="space-y-6 animate-fade-in">
      <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
        <StatCard label="Current CGPA" value={cgpaStats.cgpa} subtext="Cumulative" color="emerald" />
        <StatCard label="Credit Hours" value={cgpaStats.totalCH} subtext="Total Completed" color="blue" />
        <StatCard label="Semesters" value={profile.semesters.length} subtext="Active" color="purple" />
        <StatCard label="Degree Type" value={profile.degreeType || 'BS'} subtext="Program" color="orange" />
      </div>

      <div className="flex justify-between items-center">
        <h2 className="text-xl font-bold text-gray-800">Academic Record</h2>
        <button onClick={addSemester} className="flex items-center space-x-2 bg-emerald-600 text-white px-4 py-2 rounded-lg hover:bg-emerald-700 transition shadow-sm text-sm font-medium">
          <Plus className="h-4 w-4" />
          <span>Add Semester</span>
        </button>
      </div>

      <div className="space-y-4">
        {semesterStats.length === 0 && (
          <div className="text-center py-12 bg-gray-50 rounded-xl border-2 border-dashed border-gray-200">
            <BookOpen className="h-12 w-12 text-gray-300 mx-auto mb-3" />
            <p className="text-gray-500">No semesters added yet.</p>
            <p className="text-sm text-gray-400">Click "Add Semester" to start calculating.</p>
          </div>
        )}

        {semesterStats.map((sem, index) => (
          <div key={sem.id} className="bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden">
            <div 
              className="p-4 bg-gray-50 flex items-center justify-between cursor-pointer hover:bg-gray-100 transition-colors"
              onClick={() => setExpandedSemester(expandedSemester === sem.id ? null : sem.id)}
            >
              <div className="flex items-center space-x-4">
                <div className={`p-1 rounded-full ${expandedSemester === sem.id ? 'bg-emerald-100 text-emerald-600' : 'text-gray-400'}`}>
                  {expandedSemester === sem.id ? <ChevronUp className="h-5 w-5" /> : <ChevronDown className="h-5 w-5" />}
                </div>
                <div>
                  <h3 className="font-semibold text-gray-800">{sem.name}</h3>
                  <p className="text-xs text-gray-500">GPA: <span className="font-bold text-emerald-600">{sem.gpa}</span> • CH: {sem.totalCH}</p>
                </div>
              </div>
              <button 
                onClick={(e) => { e.stopPropagation(); removeSemester(sem.id); }}
                className="p-2 text-gray-400 hover:text-red-500 hover:bg-red-50 rounded-full transition"
              >
                <Trash2 className="h-4 w-4" />
              </button>
            </div>

            {expandedSemester === sem.id && (
              <div className="p-4 overflow-x-auto">
                <table className="w-full min-w-[600px]">
                  <thead>
                    <tr className="text-left text-xs font-semibold text-gray-500 uppercase tracking-wider border-b border-gray-100">
                      <th className="pb-2 w-1/3">Subject</th>
                      <th className="pb-2 w-20">Marks</th>
                      <th className="pb-2 w-20">Total</th>
                      <th className="pb-2 w-20">CH</th>
                      <th className="pb-2 w-20">Grade</th>
                      <th className="pb-2 w-10"></th>
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-gray-50">
                    {sem.subjects.map((sub) => (
                      <tr key={sub.id} className="group hover:bg-gray-50 transition-colors">
                        <td className="py-2 pr-2">
                          <input 
                            type="text" 
                            value={sub.name} 
                            onChange={(e) => updateSubject(sem.id, sub.id, 'name', e.target.value)}
                            className="w-full bg-transparent border-none focus:ring-0 text-sm text-gray-700 placeholder-gray-300 font-medium"
                            placeholder="Subject Name"
                          />
                        </td>
                        <td className="py-2 pr-2">
                          <input 
                            type="number" 
                            value={sub.marks} 
                            onChange={(e) => updateSubject(sem.id, sub.id, 'marks', e.target.value)}
                            className="w-full bg-gray-50 border border-gray-200 rounded px-2 py-1 text-sm focus:border-emerald-500 focus:ring-1 focus:ring-emerald-500 outline-none transition"
                            placeholder="0"
                          />
                        </td>
                        <td className="py-2 pr-2">
                          <input 
                            type="number" 
                            value={sub.total} 
                            onChange={(e) => updateSubject(sem.id, sub.id, 'total', e.target.value)}
                            className="w-full bg-gray-50 border border-gray-200 rounded px-2 py-1 text-sm focus:border-emerald-500 focus:ring-1 focus:ring-emerald-500 outline-none transition"
                            placeholder="60"
                          />
                        </td>
                        <td className="py-2 pr-2">
                          <select 
                            value={sub.ch} 
                            onChange={(e) => updateSubject(sem.id, sub.id, 'ch', e.target.value)}
                            className="w-full bg-gray-50 border border-gray-200 rounded px-2 py-1 text-sm focus:border-emerald-500 focus:ring-1 focus:ring-emerald-500 outline-none transition"
                          >
                            {[1, 2, 3, 4, 5, 6].map(n => <option key={n} value={n}>{n}</option>)}
                          </select>
                        </td>
                        <td className="py-2 text-sm font-bold text-emerald-600">
                          {calculateGradeLetter(sub.marks, sub.total, settings.gradingScale)} <span className="text-xs font-normal text-gray-400">({calculateGP(sub.marks, sub.total, settings.gradingScale).toFixed(2)})</span>
                        </td>
                        <td className="py-2 text-right">
                          <button onClick={() => removeSubject(sem.id, sub.id)} className="text-gray-300 hover:text-red-500 transition opacity-0 group-hover:opacity-100">
                            <X className="h-4 w-4" />
                          </button>
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
                <button onClick={() => addSubject(sem.id)} className="mt-3 text-xs font-medium text-emerald-600 hover:text-emerald-700 flex items-center space-x-1">
                  <Plus className="h-3 w-3" />
                  <span>Add Subject</span>
                </button>
              </div>
            )}
          </div>
        ))}
      </div>
    </div>
  );
};

const ForecasterView = ({ profile }) => {
  const [targetCGPA, setTargetCGPA] = useState(3.0);
  const [remainingCH, setRemainingCH] = useState(30);

  // Calculate current stats
  const currentStats = useMemo(() => {
    let totalQP = 0;
    let totalCH = 0;
    profile.semesters.forEach(sem => {
      sem.subjects.forEach(sub => {
        totalQP += (parseFloat(sub.ch || 0) * calculateGP(sub.marks, sub.total));
        totalCH += parseFloat(sub.ch || 0);
      });
    });
    return { qp: totalQP, ch: totalCH, cgpa: totalCH ? totalQP / totalCH : 0 };
  }, [profile]);

  const requiredGPA = useMemo(() => {
    const totalTargetQP = targetCGPA * (currentStats.ch + parseFloat(remainingCH));
    const neededQP = totalTargetQP - currentStats.qp;
    const gpa = neededQP / parseFloat(remainingCH);
    return gpa > 4.0 || gpa < 0 ? null : gpa.toFixed(2);
  }, [targetCGPA, remainingCH, currentStats]);

  return (
    <div className="max-w-2xl mx-auto space-y-6 animate-fade-in">
      <div className="bg-gradient-to-br from-emerald-600 to-teal-700 rounded-2xl p-8 text-white text-center shadow-lg">
        <h2 className="text-2xl font-bold mb-2">GPA Forecaster</h2>
        <p className="text-emerald-100 mb-6">Plan your academic future. Calculate what GPA you need to hit your target.</p>
        
        {requiredGPA !== null ? (
          <div className="bg-white/10 backdrop-blur-sm rounded-xl p-6 border border-white/20">
            <p className="text-sm font-medium uppercase tracking-wider text-emerald-200">You Need to Average</p>
            <div className="text-5xl font-extrabold my-2">{requiredGPA}</div>
            <p className="text-sm text-emerald-100">GPA in your remaining semesters</p>
          </div>
        ) : (
          <div className="bg-red-500/20 backdrop-blur-sm rounded-xl p-6 border border-red-500/30">
            <p className="font-bold text-red-100">Impossible Target</p>
            <p className="text-sm text-red-200 mt-1">Mathematically impossible to reach {targetCGPA} with given credits.</p>
          </div>
        )}
      </div>

      <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6 space-y-6">
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-2">Target CGPA Goal</label>
          <div className="flex items-center space-x-4">
            <input 
              type="range" 
              min="0" 
              max="4" 
              step="0.01" 
              value={targetCGPA} 
              onChange={(e) => setTargetCGPA(parseFloat(e.target.value))}
              className="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer accent-emerald-600"
            />
            <input 
              type="number" 
              value={targetCGPA}
              onChange={(e) => setTargetCGPA(parseFloat(e.target.value))}
              className="w-20 text-center font-bold text-emerald-600 border rounded-md p-2" 
            />
          </div>
        </div>

        <div>
          <label className="block text-sm font-medium text-gray-700 mb-2">Remaining Credit Hours</label>
          <input 
            type="number" 
            value={remainingCH}
            onChange={(e) => setRemainingCH(parseFloat(e.target.value))}
            className="w-full border border-gray-300 rounded-lg px-4 py-2 focus:ring-emerald-500 focus:border-emerald-500 transition" 
          />
          <p className="text-xs text-gray-500 mt-2">
            Currently Completed: <span className="font-medium">{currentStats.ch} CH</span> | Current CGPA: <span className="font-medium">{currentStats.cgpa.toFixed(2)}</span>
          </p>
        </div>
      </div>
    </div>
  );
};

const ProfilesView = ({ profiles, currentProfileId, setCurrentProfileId, addProfile, deleteProfile }) => (
  <div className="space-y-6 animate-fade-in">
    <div className="flex justify-between items-center">
      <h2 className="text-xl font-bold text-gray-800">Student Profiles</h2>
      <button onClick={addProfile} className="flex items-center space-x-2 bg-emerald-600 text-white px-4 py-2 rounded-lg hover:bg-emerald-700 transition shadow-sm text-sm font-medium">
        <Plus className="h-4 w-4" />
        <span>New Profile</span>
      </button>
    </div>

    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
      {profiles.map(profile => (
        <div 
          key={profile.id} 
          className={`relative bg-white rounded-xl p-5 border-2 transition-all cursor-pointer ${
            currentProfileId === profile.id 
              ? 'border-emerald-500 shadow-md ring-2 ring-emerald-100' 
              : 'border-transparent shadow-sm hover:border-emerald-200'
          }`}
          onClick={() => setCurrentProfileId(profile.id)}
        >
          <div className="flex justify-between items-start mb-3">
            <div className="h-10 w-10 bg-emerald-100 rounded-full flex items-center justify-center text-emerald-600 font-bold text-lg">
              {profile.name.charAt(0)}
            </div>
            {profiles.length > 1 && (
              <button 
                onClick={(e) => { e.stopPropagation(); deleteProfile(profile.id); }}
                className="text-gray-300 hover:text-red-500 transition"
              >
                <Trash2 className="h-4 w-4" />
              </button>
            )}
          </div>
          <h3 className="font-bold text-gray-800 truncate">{profile.name}</h3>
          <p className="text-xs text-gray-500 mb-4 font-mono">{profile.agNumber || 'No Registration #'}</p>
          <div className="flex items-center justify-between text-xs font-medium bg-gray-50 p-2 rounded-lg">
            <span className="text-gray-500">{profile.semesters.length} Semesters</span>
            <span className="text-emerald-600">{profile.degreeType || 'BS'}</span>
          </div>
          {currentProfileId === profile.id && (
            <div className="absolute top-2 right-2">
              <span className="flex h-3 w-3">
                <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
                <span className="relative inline-flex rounded-full h-3 w-3 bg-emerald-500"></span>
              </span>
            </div>
          )}
        </div>
      ))}
    </div>
  </div>
);

const ImportView = ({ importData }) => {
  const [agNumber, setAgNumber] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleImport = async (e) => {
    e.preventDefault();
    if (!agNumber) return;
    setLoading(true);
    setError('');

    // Simulation of API Call
    setTimeout(() => {
      // In a real app, fetch(API_BASE_URL + '/result?reg=' + agNumber)
      try {
        // Mock success
        const mockData = {
          name: "Imported Student",
          agNumber: agNumber,
          degreeType: "BS",
          semesters: [
            {
              id: generateId(),
              name: "Semester 1",
              subjects: [
                { id: generateId(), name: "Intro to Computing", marks: 45, total: 60, ch: 3 },
                { id: generateId(), name: "English I", marks: 50, total: 60, ch: 3 },
              ]
            }
          ]
        };
        importData(mockData);
        setLoading(false);
        setAgNumber('');
        alert("Data imported successfully!");
      } catch (err) {
        setError("Failed to fetch data. Please try again.");
        setLoading(false);
      }
    }, 1500);
  };

  return (
    <div className="max-w-md mx-auto space-y-6 animate-fade-in py-10">
      <div className="text-center">
        <div className="bg-emerald-100 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4">
          <Download className="h-8 w-8 text-emerald-600" />
        </div>
        <h2 className="text-xl font-bold text-gray-800">Import Results</h2>
        <p className="text-sm text-gray-500 mt-2">Enter your AG Number to fetch results directly from UAF servers.</p>
      </div>

      <form onSubmit={handleImport} className="bg-white p-6 rounded-xl shadow-sm border border-gray-200">
        <div className="space-y-4">
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">Registration Number</label>
            <input 
              type="text" 
              placeholder="e.g. 2020-ag-1234"
              value={agNumber}
              onChange={(e) => setAgNumber(e.target.value)}
              className="w-full border border-gray-300 rounded-lg px-4 py-2 focus:ring-emerald-500 focus:border-emerald-500 outline-none"
            />
          </div>
          
          {error && <div className="text-xs text-red-500">{error}</div>}

          <button 
            type="submit" 
            disabled={loading || !agNumber}
            className={`w-full py-2.5 rounded-lg text-white font-medium shadow-sm transition-all flex justify-center items-center space-x-2 ${loading ? 'bg-gray-400 cursor-not-allowed' : 'bg-emerald-600 hover:bg-emerald-700'}`}
          >
            {loading ? (
              <span>Connecting...</span>
            ) : (
              <>
                <Download className="h-4 w-4" />
                <span>Fetch Result</span>
              </>
            )}
          </button>
        </div>
      </form>
      <p className="text-xs text-center text-gray-400">Note: Requires active internet connection.</p>
    </div>
  );
};

const SettingsView = ({ settings, updateSettings }) => (
  <div className="max-w-2xl mx-auto space-y-6 animate-fade-in">
    <h2 className="text-xl font-bold text-gray-800">Application Settings</h2>
    
    <div className="bg-white rounded-xl shadow-sm border border-gray-200 divide-y divide-gray-100">
      <div className="p-6">
        <div className="flex items-center justify-between mb-2">
          <div>
            <h3 className="font-medium text-gray-900">Grading System</h3>
            <p className="text-xs text-gray-500">Select the calculation method used by your department.</p>
          </div>
          <Settings className="h-5 w-5 text-gray-400" />
        </div>
        <div className="mt-4 grid grid-cols-2 gap-3">
          <button 
            onClick={() => updateSettings({ ...settings, gradingScale: 'modern' })}
            className={`p-3 rounded-lg border text-sm font-medium text-left transition-all ${settings.gradingScale === 'modern' ? 'border-emerald-500 bg-emerald-50 text-emerald-700' : 'border-gray-200 hover:bg-gray-50'}`}
          >
            <div className="font-bold">HEC / Modern</div>
            <div className="text-xs opacity-75 font-normal mt-1">50% Passing Marks. Standard 4.0 Scale.</div>
          </button>
          <button 
            onClick={() => updateSettings({ ...settings, gradingScale: 'legacy' })}
            className={`p-3 rounded-lg border text-sm font-medium text-left transition-all ${settings.gradingScale === 'legacy' ? 'border-emerald-500 bg-emerald-50 text-emerald-700' : 'border-gray-200 hover:bg-gray-50'}`}
          >
            <div className="font-bold">Legacy Scheme</div>
            <div className="text-xs opacity-75 font-normal mt-1">40% Passing Marks. Progressive Scale.</div>
          </button>
        </div>
      </div>

      <div className="p-6">
        <h3 className="font-medium text-gray-900 mb-4">About</h3>
        <p className="text-sm text-gray-500 leading-relaxed">
          This calculator uses the latest algorithms consistent with University of Agriculture Faisalabad (UAF) examination policies. 
          While we strive for 100% accuracy, please verify official results from the controller of examinations.
        </p>
      </div>
    </div>
  </div>
);

// --- Main Application ---

export default function App() {
  const [isSidebarOpen, setIsSidebarOpen] = useState(false);
  const [activeTab, setActiveTab] = useState('calculator');
  const [serverStatus, setServerStatus] = useState(true);
  
  // State: Profiles
  const [profiles, setProfiles] = useState(() => {
    const saved = localStorage.getItem('uaf_profiles');
    return saved ? JSON.parse(saved) : [{
      id: 'default',
      name: 'My Profile',
      agNumber: '',
      degreeType: 'BS',
      semesters: []
    }];
  });

  const [currentProfileId, setCurrentProfileId] = useState(() => {
    return localStorage.getItem('uaf_current_profile_id') || 'default';
  });

  // State: Settings
  const [settings, setSettings] = useState(() => {
    const saved = localStorage.getItem('uaf_settings');
    return saved ? JSON.parse(saved) : { gradingScale: 'modern' };
  });

  // Effect: Persistence
  useEffect(() => {
    localStorage.setItem('uaf_profiles', JSON.stringify(profiles));
    localStorage.setItem('uaf_current_profile_id', currentProfileId);
    localStorage.setItem('uaf_settings', JSON.stringify(settings));
  }, [profiles, currentProfileId, settings]);

  // Effect: Server Heartbeat Simulation
  useEffect(() => {
    const interval = setInterval(() => {
      // Simulate checking server status
      setServerStatus(Math.random() > 0.05); // 95% uptime sim
    }, 10000);
    return () => clearInterval(interval);
  }, []);

  // Helpers
  const currentProfile = profiles.find(p => p.id === currentProfileId) || profiles[0];

  const updateProfile = (updatedProfile) => {
    setProfiles(profiles.map(p => p.id === updatedProfile.id ? updatedProfile : p));
  };

  const addProfile = () => {
    const newId = generateId();
    const newProfile = {
      id: newId,
      name: `Student ${profiles.length + 1}`,
      agNumber: '',
      degreeType: 'BS',
      semesters: []
    };
    setProfiles([...profiles, newProfile]);
    setCurrentProfileId(newId);
    setActiveTab('calculator');
  };

  const deleteProfile = (id) => {
    if (profiles.length <= 1) {
      alert("Cannot delete the last profile.");
      return;
    }
    const newProfiles = profiles.filter(p => p.id !== id);
    setProfiles(newProfiles);
    setCurrentProfileId(newProfiles[0].id);
  };

  const importData = (data) => {
    const newProfile = { ...data, id: generateId() };
    setProfiles([...profiles, newProfile]);
    setCurrentProfileId(newProfile.id);
    setActiveTab('calculator');
  };

  return (
    <div className="min-h-screen bg-gray-50 flex flex-col font-sans text-gray-900">
      <Header toggleSidebar={() => setIsSidebarOpen(!isSidebarOpen)} serverStatus={serverStatus} />
      
      <div className="flex flex-1 overflow-hidden relative">
        <Sidebar 
          isOpen={isSidebarOpen} 
          activeTab={activeTab} 
          setActiveTab={setActiveTab} 
          closeSidebar={() => setIsSidebarOpen(false)} 
        />
        
        <main className="flex-1 overflow-y-auto p-4 lg:p-8 relative w-full">
          <div className="max-w-5xl mx-auto pb-10">
            {activeTab === 'calculator' && (
              <CalculatorView 
                profile={currentProfile} 
                updateProfile={updateProfile} 
                settings={settings}
              />
            )}
            {activeTab === 'forecast' && (
              <ForecasterView profile={currentProfile} />
            )}
            {activeTab === 'profiles' && (
              <ProfilesView 
                profiles={profiles} 
                currentProfileId={currentProfileId}
                setCurrentProfileId={setCurrentProfileId}
                addProfile={addProfile}
                deleteProfile={deleteProfile}
              />
            )}
            {activeTab === 'import' && (
              <ImportView importData={importData} />
            )}
            {activeTab === 'settings' && (
              <SettingsView settings={settings} updateSettings={setSettings} />
            )}
          </div>
        </main>
      </div>

      <footer className="bg-white border-t border-gray-200 py-4 text-center text-xs text-gray-400">
        <p>© {new Date().getFullYear()} UAF CGPA Calculator. All rights reserved.</p>
      </footer>
    </div>
  );
}
