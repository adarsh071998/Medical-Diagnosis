import pymysql
pymysql.install_as_MySQLdb()

"""
data = {}
data['user_id']='Guest'
data['sex']='M'
data['age']=16

data['rbc']=3.9
data['wbc']=6
data['hgb']=12
data['hct']=35
data['mcv']=84
data['mch']=30
data['mchc']=200
data['chcm']=34.8
data['rdw']=14
data['hdw']=3
data['plt']=200
data['mpv']=8
data['neu']=60
data['lymph']=20
data['mono']=6
data['eosin']=3
data['baso']=0.5
"""
def CBC(data):
	result = {}
	conn = pymysql.connect(host='localhost',database='medical',user='root',password='satpute@123')
	cursor = conn.cursor(pymysql.cursors.DictCursor)
	try:
		if data['user_id']!='Guest':
			cursor.execute("select *from users where user_id="+"'"+data['user_id']+"'")
			rows=cursor.fetchone()
			for row in rows:
				print(row)
			data['age']=rows['age']
			data['sex']=rows['sex']		
		print(data)
		if data['sex']=='M':
			sql = "select *from male where %s between min_age and max_age"
			cursor.execute(sql,int((data['age'])))
			rows=cursor.fetchone()
			if data['rbc'] < rows['min_rbc']:
				result['rbc']=data['rbc']
				result['min_rbc']=rows['min_rbc']
				result['max_rbc']=rows['max_rbc']
				result['rbc_con']='low'
				result['rbc_reason']='anemiabone marrow failure erythropoietin deficiency, which is the primary cause of anemia in patients with chronic kidney disease hemolysis, or RBC destruction caused by transfusions and blood vessel injury internal or external bleeding pregnancy'
				result['rbc_remedies']='Iron: Eating an iron-rich diet can increase your bodys production of RBCs. Iron-rich foods include: red meat, such as beef organ meat, such as kidney and liverdark, leafy, green vegetables, such as spinach and kale dried fruits, such as prunes and raisins beans legumes egg yolks'

			elif data['rbc'] > rows['max_rbc']:
				result['rbc']=data['rbc']
				result['min_rbc']=rows['min_rbc']
				result['max_rbc']=rows['max_rbc']
				result['rbc_con']='high'
				result['rbc_reason']='Low oxygen levels Your body may increase red blood cell production to compensate for any condition that results in low oxygen levels. including  Heart disease (such as congenital heart disease in adults). Heart failure: A condition present at birth that reduces the oxygen-carrying capacity of red blood cells (hemoglobinopathy)'
				result['rbc_remedies']='Stop Smoking,  Phlebotomy or Blood Draw, A procedure that removes some blood from the body. A needle is inserted into one of the veins and blood from the vein flows through an airtight tube into a sterile container or bag. The process is similar to the process of donating blood.'

			if data['wbc'] < rows['min_wbc']:
				result['wbc']=data['wbc']
				result['min_wbc']=rows['min_wbc']
				result['max_wbc']=rows['max_wbc']
				result['wbc_con']='low'
				result['desc'] = ''
				result['wbc_reason']='Bone marrow problems:   Low WBC counts are often linked to bone marrow problems. Being around certain chemicals, like benzene and pesticides, as well as some types of cancer and cancer treatments including chemotherapy and radiation, can hurt your bone marrow s ability to make WBCs.'
				result['wbc_remedies']='Medications called growth factors can be used preventively before chemotherapy to boost white blood cell count, Popular citrus fruits include: grapefruit,oranges,tangerines,lemons,limes,clementines, kiwi etc.'
			
			elif data['wbc'] > rows['max_wbc']:
				result['wbc']=data['wbc']
				result['min_wbc']=rows['min_wbc']
				result['max_wbc']=rows['max_wbc']
				result['wbc_con']='high'
				result['wbc_reason']='Severe Stress, Drug Reactions, Infections, Inflammationns'
				result['wbc_remedies']=' Eat healthy foods to support and strengthen your immune system. Fruits, vegetables, garlic and mitake or shitake mushrooms are packed full of powerful immune boosters. Avoid soda and fried and processed foods, which will weaken your immunity. Avoid stress by exercising and getting plenty of sleep. Talk with your doctor about medications you are taking that could raise your WBC count.'

			if data['hgb'] < rows['min_hgb']:
				result['hgb']=data['hgb']
				result['min_hgb']=rows['min_hgb']
				result['max_hgb']=rows['max_hgb']
				result['hgb_con']='low'
				result['hgb_reason']='loss of blood (traumatic injury, surgery, bleeding, colon cancer, or stomach ulcer), nutritional deficiency (iron, vitamin B12, folate), bone marrow problems (replacement of bone marrow by cancer), suppression by red blood cell synthesis bychemotherapy drugs, kidney failure, and abnormal hemoglobin structure (sickle cell anemia or thalassemia)'
				result['hgb_remedies']="""Eat Iron-Rich Foods, Increase Vitamin C ,Intake Increase Folic Acid Intake, An Apple (or Pomegranate) a Day Keeps The Doctor Away, Drink Nettle Tea, Avoid Iron Blockers, Exercise"""


			elif data['hgb'] > rows['max_hgb']:
				result['hgb']=data['hgb']
				result['min_hgb']=rows['min_hgb']
				result['max_hgb']=rows['max_hgb']
				result['hgb_con']='high'
				result['hgb_reason']='COPD (chronic obstructive pulmonary disease), Dehydration, Emphysema, Heart failure, Kidney cancer, Liver cancer, Living at a high altitude, where there s less oxygen in the air, Other types of heart disease, Other types of lung diseasem, Polycythemia vera, Smoking, which may result in low blood oxygen levels'
				result['hgb_remedies']='Hydration, Quit Smoking , Bloodletting'

			if data['hct'] < rows['min_hct']:
				result['hct']=data['hct']
				result['min_hct']=rows['min_hct']
				result['max_hct']=rows['max_hct']
				result['hct_con']='low'
				result['hct_reason']='Bleeding (ulcers, trauma, colon cancer, internal bleeding), Destruction of red blood cells (sickle cell anemia, enlarged spleen), Decreased production of red blood cells (bone marrow supression, cancer, drugs), Nutritional problems (low iron, B 12, folate and malnutrition), Overhydration (polydypsia, intravenous overhydration)'
				result['hct_remedies']='Eat a healthy and balanced diet. Do not be overly concerned about lowered hematocrit levels. Normal hematocrit levels can vary depending on several factors such as gender and even geographical location. Eating a healthy and balanced diet with foods high in iron can increase the bloods capacity to carry oxygen and meet body demands. Exercise regularly. Exercise helps the body to produce red blood cells because the bodys need for oxygen and nutrients increases during exercise. Take vitamin and mineral supplements. This keeps the body in good general health and aids in the absorption of iron in the body.'

			elif data['hct'] > rows['max_hct']:
				result['hct']=data['hct']
				result['min_hct']=rows['min_hct']
				result['max_hct']=rows['max_hct']
				result['hct_con']='high'
				result['hct_reason']='Dehydration (heat exhaustion, no available source of fluids), Low availability of oxygen (smoking, high altitude, pulmonary fibrosis), Genetic (congenital heart diseases), Erythrocytosis (over-production of red blood cells by the bone marrow or polycythemia vera), Cor pulmonale (COPD, chronic sleep apnea, pulmonary embolisms)'
				result['hct_remedies']='Avoid taking iron supplements, Stay hydrated, Know what drinks to avoid, Eat grapefruit every day, Get more anti-oxidants., Exercise in moderation, Donate blood., Stop smoking.'	
		

			if data['mcv'] < rows['min_mcv']:
				result['mcv']=data['mcv']
				result['min_mcv']=rows['min_mcv']
				result['max_mcv']=rows['max_mcv']
				result['mcv_con']='low'
				result['mcv_reason']='Iron deficiency anemia, Anemia of chronic disease, Thalassemia, Sideroblastic anemia'
				result['mcv_remedies']=''

			elif data['mcv'] > rows['max_mcv']:
				result['mcv']=data['mcv']
				result['min_mcv']=rows['min_mcv']
				result['max_mcv']=rows['max_mcv']
				result['mcv_con']='high'
				result['mcv_reason']='Folate deficiency anemia, Vitamin B12 deficiency anemia, Liver diseasem, Hemolytic anemias, Hypothyroidism, Excessive alcohol intake, Aplastic anemia, Myelodysplastic syndrome'
				result['mcv_remedies']=''

			if data['mch'] < rows['min_mch']:
				result['mch']=data['mch']
				result['min_mch']=rows['min_mch']
				result['max_mch']=rows['max_mch']
				result['mch_con']='low'
				result['mch_reason']='Iron deficiency anemia, Anemia of chronic disease, Thalassemia, Sideroblastic anemia'
				result['mch_remedies']=''

			elif data['mch'] > rows['max_mch']:
				result['mch']=data['mch']
				result['min_mch']=rows['min_mch']
				result['max_mch']=rows['max_mch']
				result['mchc_con']='high'
				result['mch_reason']='Folate deficiency anemia, Vitamin B12 deficiency anemia, Liver diseasem, Hemolytic anemias, Hypothyroidism, Excessive alcohol intake, Aplastic anemia, Myelodysplastic syndrome'
				result['mch_remedies']=''	

			 
			if data['mchc'] < rows['min_mchc']:
				result['mchc']=data['mchc']
				result['min_mchc']=rows['min_mchc']
				result['max_mchc']=rows['max_mchc']
				result['mchc_con']='low'
				result['mchc_reason']='Iron deficiency anemia, Anemia of chronic disease, Thalassemia, Sideroblastic anemia'
				result['mchc_remedies']=''

			elif data['mchc'] > rows['max_mchc']:
				result['mchc']=data['mchc']
				result['min_mchc']=rows['min_mchc']
				result['max_mchc']=rows['max_mchc']
				result['mchc_con']='high'
				result['mchc_reason']='Folate deficiency anemia, Vitamin B12 deficiency anemia, Liver diseasem, Hemolytic anemias, Hypothyroidism, Excessive alcohol intake, Aplastic anemia, Myelodysplastic syndrome, Two exceptions in spherocytosis, the MCHC is elevated but not in pernicious anemia.'
				result['mchc_remedies']=''	
			
			if data['chcm'] < rows['min_chcm']:
				result['chcm']=data['chcm']
				result['min_chcm']=rows['min_chcm']
				result['max_chcm']=rows['max_chcm']
				result['chcm_con']='low'
				result['chcm_reason']=''
				result['chcm_remedies']=''

			elif data['chcm'] > rows['max_chcm']:
				result['chcm']=data['chcm']
				result['min_chcm']=rows['min_chcm']
				result['max_chcm']=rows['max_chcm']
				result['chcm_con']='high'
				result['chcm_reason']=''
				result['chcm_remedies']=''

			if data['rdw'] < rows['min_rdw']:
				result['rdw']=data['rdw']
				result['min_rdw']=rows['min_rdw']
				result['max_rdw']=rows['max_rdw']
				result['rdw_con']='low'
				result['rdw_reason']='Iron deficiency anemia (blood loss, parasites, poor iron absorption, etc.), Vitamin B6 anemia, Rheumatoid arthritis'
				result['rdw_remedies']=''

			elif data['rdw'] > rows['max_rdw']:
				result['rdw']=data['rdw']
				result['min_rdw']=rows['min_rdw']
				result['max_rdw']=rows['max_rdw']
				result['rdw_con']='high'
				result['rdw_reason']='B12 and Pernicious anemia, Folic acid anemiaIron deficiency anemia combined with other anemia, Hemolytic anemia, Transfusions, Sideroblastic anemia, Alcohol abuse, Various less common and hereditary anemias'
				result['rdw_remedies']=''

			if data['hdw'] < rows['min_hdw']:
				result['hdw']=data['hdw']
				result['min_hdw']=rows['min_hdw']
				result['max_hdw']=rows['max_hdw']
				result['hdw_con']='low'
				result['hdw_reason']='loss of blood (traumatic injury, surgery, bleeding, colon cancer, or stomach ulcer), nutritional deficiency (iron, vitamin B12, folate), bone marrow problems (replacement of bone marrow by cancer), suppression by red blood cell synthesis bychemotherapy drugs, kidney failure, and abnormal hemoglobin structure (sickle cell anemia or thalassemia)'
				result['hdw_remedies']='Eat Iron-Rich Foods, Increase Vitamin C ,Intake Increase Folic Acid Intake, An Apple (or Pomegranate) a Day Keeps The Doctor Away, Drink Nettle Tea, Avoid Iron Blockers, Exercise'

			elif data['hdw'] > rows['max_hdw']:
				result['hdw']=data['hdw']
				result['min_hdw']=rows['min_hdw']
				result['max_hdw']=rows['max_hdw']
				result['hdw_con']='high'
				result['hdw_reason']='COPD (chronic obstructive pulmonary disease), Dehydration, Emphysema, Heart failure, Kidney cancer, Liver cancer, Living at a high altitude, where there s less oxygen in the air, Other types of heart disease, Other types of lung diseasem, Polycythemia vera, Smoking, which may result in low blood oxygen levels'
				result['hdw_remedies']='Hydration, Quit Smoking , Bloodletting'

			if data['plt'] < rows['min_plt']:
				result['plt']=data['plt']
				result['min_plt']=rows['min_plt']
				result['max_plt']=rows['max_plt']
				result['plt_con']='low'
				result['plt_reason']='Marrow depression (aplastic anemia, radiation, chemotherapy, drugs), Marrow infiltration (acute leukemia, carcinoma, myelofibrosis, multiple myeloma), Megaloblastic anemia (B12 and/or folic acid deficiency), CongenitalIncreased Destruction'
				result['plt_remedies']=''

			elif data['plt'] > rows['max_plt']:
				result['plt']=data['plt']
				result['min_plt']=rows['min_plt']
				result['max_plt']=rows['max_plt']
				result['plt_con']='high'
				result['plt_reason']='InfectionAcute blood loss, Disseminated carcinoma, Splenectomy, Various free radical pathologies (tissue damage, chronic inflammation, surgery), Thrombocythemia, ,, Polycythemia Vera, Myeloproliferative Disorders, Chronic Granulocytic Leukemia, Hemolytic anemia(s), Myelosclerosis, Essential (without known cause)'
				result['plt_remedies']=''



			
			if data['mpv'] < rows['min_mpv']:
				result['mpv']=data['mpv']
				result['min_mpv']=rows['min_mpv']
				result['max_mpv']=rows['max_mpv']
				result['mpv_con']='low'
				result['mpv_reason']='A low MPV means your platelets are smaller than average. Smaller platelets tend to be older, so a low MPV could mean your bone marrow isn t producing enough new ones, a low MPV could indicate: inflammatory bowel disease, including Crohn s disease or ulcerative colitis cytotoxic medications, which are used in chemotherapy aplastic anemia'
				result['mpv_remedies']=''

			elif data['mpv'] > rows['max_mpv']:
				result['mpv']=data['chcm']
				result['min_mpv']=rows['min_mpv']
				result['max_mpv']=rows['max_mpv']
				result['mpv_con']='high'
				result['mpv_reason']='A high MPV means that your platelets are larger than average. This is sometimes a sign that you re producing too many platelets. A high MPV suggests increased platelet production, which is associated with reduced survival rates in several types of cancer, including: lung cancer, ovarian cancer,endometrial cancer, colon cancer, kidney cancer, stomach cancer, pancreatic cancer, breast cancer'
				result['mpv_remedies']=''


			if data['neu'] < rows['min_neu']:
				result['neu']=data['neu']
				result['min_neu']=rows['min_neu']
				result['max_neu']=rows['max_neu']
				result['neu_con']='low'
				result['neu_reason']='some drugs, including those used in chemotherapy, suppressed immune system, bone marrow failure, aplastic anemia, febrile neutropenia, which is a medical emergency, congenital disorders, such as Kostmann syndrome and cyclic neutropenia, hepatitis A, B, or C, HIV/AIDS, sepsis, autoimmune diseases, including rheumatoid arthritis'
				result['neu_remedies']=''

			elif data['neu'] > rows['max_neu']:
				result['neu']=data['neu']
				result['min_neu']=rows['min_neu']
				result['max_neu']=rows['max_neu']
				result['neu_con']='high'
				result['neu_reason']='infection, most likely bacterial, noninfectious inflammation, injury, surgery, smoking cigarettes or sniffing tobacco, high stress level, excessive exercise, steroid use, heart attacks'
				result['neu_remedies']=''



			if data['lymph'] < rows['min_lymph']:
				result['lymph']=data['chcm']
				result['min_lymph']=rows['min_lymph']
				result['max_lymph']=rows['max_lymph']
				result['lymph_con']='low'
				result['lymph_reason']='A low lymphocyte count, called lymphocytopenia, usually occurs because:,your body isnt producing enough lymphocytes,lymphocytes are being destroyed,lymphocytes are,trapped in your spleen or lymph nodes,undernutrition,HIV and AIDS,influenza autoimmune conditions, such as lupus some cancers, including lymphocytic anemia, lymphoma, and Hodgkin disease steroid use radiation therapy certain drugs, including chemotherapy drugs'
				result['lymph_remedies']=''

			elif data['lymph'] > rows['max_lymph']:
				result['lymph']=data['lymph']
				result['min_lymph']=rows['min_lymph']
				result['max_lymph']=rows['max_lymph']
				result['lymph_con']='high'
				result['lymph_reason']='Lymphocytosis, or a high lymphocyte count, is common if youve had an infection. High lymphocyte levels that persist may point to a more serious illness or disease, such as: viral infections, including measles, mumps, and mononucleosis adenovirus, hepatitis, influenza, tuberculosis, toxoplasmosis, cytomegalovirus, brucellosis, vasculitis, acute lymphocytic leukemia, chronic lymphocytic leukemia, HIV and AIDS'
				result['lymph_remedies']=''


			if data['mono'] < rows['min_mono']:
				result['mono']=data['mono']
				result['min_mono']=rows['min_mono']
				result['max_mono']=rows['max_mono']
				result['mono_con']='low'
				result['mono_reason']='Monocytopenia Lowers the Risk of Cardiovascular Disease, Monocytopenia Increases Susceptibility to Infections, Monocytopenia is Associated with a Risk of Hematologic Disorders, Monocytopenia Increases Risk of Cervical Cancer'
				result['mono_remedies']='Acute Strenuous Exercise, Sauna :This is because overheating the human body leads to elevated activity of monocytes, Cold Exposure, Growth Hormone, Menopause, Testosterone, Garlic'

			elif data['mono'] > rows['max_mono']:
				result['mono']=data['chcm']
				result['min_mono']=rows['min_mono']
				result['max_mono']=rows['max_mono']			
				result['mono_con']='high'
				result['mono_reason']='Monocytosis Increases Risk of Atherosclerosis, Monocytosis May Increase Inflammation in Diabetes, Monocytosis is Associated with Increased Risk of Death in the Elderly, Monocytosis Facilitates Healing Process After a Heart Attack'
				result['mono_remedies']='Acute Alcohol Intake, regular Exercise, Weight Loss, Omega-3 Fatty Acids, Mediterranean Diet'

			if data['eosin'] < rows['min_eosin']:
				result['eosin']=data['eosin']
				result['min_eosin']=rows['min_eosin']
				result['max_eosin']=rows['max_eosin']
				result['eosin_con']='low'
				result['eosin_reason']=''
				result['eosin_remedies']=''

			elif data['eosin'] > rows['max_eosin']:
				result['eosin']=data['eosin']
				result['min_eosin']=rows['min_eosin']
				result['max_eosin']=rows['max_eosin']
				result['eosin_con']='high'
				result['eosin_reason']='an infection by parasitic worms, an autoimmune disease, severe allergic reactions, eczema, asthma, seasonal allergies, leukemia and certain other cancers, ulcerative colitis, scarlet fever, lupus, Crohns disease, a significant drug reaction, an organ transplant rejection'
				result['eosin_remedies']='Ginger: it is very good herb in lowering down the increase count of eosinophils. Turmeric powder: it is very good remedy to treat patients who have higher values of eosinophils. Ginseng: it is very good home remedy in reducing the inflammation in airways and thus lowers down the count of high eosinophils.'


			if data['baso'] < rows['min_baso']:
				result['baso']=data['baso']
				result['min_baso']=rows['min_baso']
				result['max_baso']=rows['max_baso']
				result['baso_con']='low'
				result['baso_reason']='Hyperthyroidism: This happens when your thyroid gland produces too much thyroid hormone. The excess hormone causes your bodily functions to speed up. Symptoms include an: increased heart rate, increased blood pressure, excessive sweating, weight loss. Infections: This occurs when bacteria or other harmful substances enter an injured part of the body. Symptoms run the gamut from pus and pain when touched to fever and diarrhea. Acute hypersensitivity reactions: In this case, your body overreacts to a substance in the form of an acute allergic reaction. Symptoms include: watery eyes, runny nose , red rash and itchy hives'
				result['baso_remedies']=''

			elif data['baso'] > rows['max_baso']:
				result['baso']=data['baso']
				result['min_baso']=rows['min_baso']
				result['max_baso']=rows['max_baso']
				result['baso_con']='high'
				result['baso_reason']='Hypothyroidism: This occurs when your thyroid gland doesnt produce enough thyroid hormone. If your thyroid hormone is low, it can cause your bodily functions to slow down. Symptoms include: puffy face, hoarse voice, brittle hair, coarse skin, weight gain. Myeloproliferative disorders: This refers to a group of conditions that cause too many white blood cells, red blood cells, or platelets be to produced in your bone marrow. Autoimmune inflammation: This occurs when your immune system attacks your own body. Symptoms include: inflamed joints, fever, hair loss, muscle pain'
				result['baso_remedies']=''


		return result
	except:
		return ('{"type":"rcbc","desc":"Invalid data"}')
#print(CBC(data))	