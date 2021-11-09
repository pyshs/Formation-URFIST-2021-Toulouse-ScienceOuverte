nombre_articles = 0
motcle = "COVID"
titres = ["E. Meriglier, C. Rivoisy, Mojgan Hessamfar, N. Bernard, I. Aureau, et al.. Safety of hydroxychloroquine and darunavir or lopinavir in COVID-19 infection. Journal of Antimicrobial Chemotherapy, Oxford University Press (OUP), 2021, 76 (2), pp.482-486. &#x27E8;10.1093/jac/dkaa441&#x27E9;. &#x27E8;hal-03165515&#x27E9;",
"Thibault Fiolet, Anthony Guihur, Mathieu Edouard Rebeaud, Matthieu Mulot, Nathan Peiffer-Smadja, et al.. Effect of hydroxychloroquine with or without azithromycin on the mortality of coronavirus disease 2019 (COVID-19) patients: a systematic review and meta-analysis. Clinical Microbiology and Infection, Elsevier for the European Society of Clinical Microbiology and Infectious Diseases, 2021, 27 (1), pp.19-27. &#x27E8;10.1016/j.cmi.2020.08.022&#x27E9;. &#x27E8;hal-03127508&#x27E9;",
"Federico Perche, Y. Yi, L. Hespel, P Mi, A Dirisala, et al.. Hydroxychloroquine-conjugated gold nanoparticles for improved siRNA activity. Biomaterials, Elsevier, 2016, 90, pp.62-71. &#x27E8;10.1016/j.biomaterials.2016.02.027&#x27E9;. &#x27E8;hal-02130728&#x27E9;",
"Maryse Lepoittevin. Intérêt comparé de l’imagerie et de l’électrorétinographie multifocale dans le suivi des patients traités par Chloroquine ou Hydroxychloroquine. Médecine humaine et pathologie. 2015. &#x27E8;dumas-01243546&#x27E9;",
"M. Cour, C. Amaz, J. Bohe, T. Rimmele, M. Ovize, et al.. Day-90 survival in critically-ill patients with COVID-19 and hydroxychloroquine: a propensity analysis. Annals of translational medicine, AME Publishing Company, 2021, 9 (7), pp.524. &#x27E8;10.21037/atm-20-7811&#x27E9;. &#x27E8;inserm-03337966&#x27E9;",
"Guillaume Binson, Nicolas Venisse, Alexis Sauvaget, Astrid Bacle, Pauline Lazaro, et al.. Preparation and physicochemical stability of 50 mg/mL hydroxychloroquine oral suspension in SyrSpend(Ⓡ) SF PH4 (dry). International Journal of Antimicrobial Agents, Elsevier, 2020, 56 (6), pp.106201. &#x27E8;10.1016/j.ijantimicag.2020.106201&#x27E9;. &#x27E8;hal-03003546&#x27E9;"]
nombre_total_articles = len(titres)
if nombre_total_articles > 0:
    for i in titres:
        if motcle in i:
            print(i)
            nombre_articles+=1
else:
    print("La liste est vide")
proportion = 100*nombre_articles/nombre_total_articles
print("Proportion d'articles contenant le terme dans le titre : {} %".format(round(proportion,1)))
