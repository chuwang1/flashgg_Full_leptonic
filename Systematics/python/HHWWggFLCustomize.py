import FWCore.ParameterSet.Config as cms

class HHWWggCustomize():
    """
    HH->WWgg process customizaton class. Started with HH->bbgg customization class. 
    """
    
    def __init__(self, process, customize, metaConditions):
        self.process = process
        self.customize = customize
        self.metaConditions = metaConditions
        # self.tagList = [ ["HHWWggFLTag",12] ]
        self.tagList = [ ["HHWWggFLTag",4] ]
        self.customizeTagSequence()

    def variablesToDump(self):

        ##- Variables for the nominal output tag tree (non systematic trees for each category)
        variables = []

        # Cut flow variables 
        cutFlowVars = [
            "passPS[2,0,2] := Cut_Variables[0]",
            "passPhotonSels[2,0,2] := Cut_Variables[1]",
            "passGoodEle[2,0,2] := Cut_Variables[2]",
            "passGoodMuon[2,0,2] := Cut_Variables[3]",
            "ExTwoEle[2,0,2] := Cut_Variables[4]",
            "ExTwoMuon[2,0,2] := Cut_Variables[5]",
            "ExTwoDiffLep[2,0,2] := Cut_Variables[6]",
            "ExTwoLep[2,0,2] := Cut_Variables[7]",
            "ExOneLep[2,0,2] := Cut_Variables[8]",
            "AtLeastOneLep[2,0,2] := Cut_Variables[9]",
            "ExTwoLepAfterDR[2,0,2] := Cut_Variables[11]",
            "passDR[2,0,2] := Cut_Variables[10]",
            "MetCut[2,0,2] := Cut_Variables[12]"
        ]

        # b scores
        bScores = [] 
        for jeti in range(0,6):
            var1 = "jet" + str(jeti) + "_DeepFlavourScore[2,0,2] := ? JetVector.size() >= " + str(jeti + 1) + " ? JetVector[" + str(jeti) + "].bDiscriminator('mini_pfDeepFlavourJetTags:probb') : -99 "
            var2 = "jet" + str(jeti) + "_DeepCSVScore[2,0,2] := ? JetVector.size() >= " + str(jeti + 1) + " ? JetVector[" + str(jeti) + "].bDiscriminator('pfDeepCSVJetTags:probb') : -99 "
            bScores.append(var1)
            bScores.append(var2)

        # inital / final photon energies for scaling and smearing validation
        phoEs = [
          "lp_E[100,0,100] := Leading_Photon.p4().E()",
          "slp_E[100,0,100] := Subleading_Photon.p4().E()",
          "lp_initE[100,0,100] := Leading_Photon.energyAtStep('initial')",
          "slp_initE[100,0,100] := Subleading_Photon.energyAtStep('initial')", # also want final energies 
        ]
        Reco_var =[
          "lp_pt                               := Leading_Photon.p4().pt()",       
          "lp_eta                              := Leading_Photon.p4().eta()",
          "lp_SC_eta                           := Leading_Photon.superCluster().eta()",
          "lp_phi                              := Leading_Photon.p4().phi()",
          "lp_E                                := Leading_Photon.p4().E()",
          "lp_initE                            := Leading_Photon.energyAtStep('initial')",
          "lp_r9                               := Leading_Photon.old_r9()",
          "lp_full5x5_r9                       := Leading_Photon.full5x5_r9()",
          "lp_Hgg_MVA                          := lp_Hgg_MVA()",
          "lp_passElectronVeto                 := Leading_Photon.passElectronVeto()",
          "lp_hasPixelSeed                     := Leading_Photon.hasPixelSeed",
          # Subleading Photon
          # slp = Subleading Photon 
          "slp_pt                              := Subleading_Photon.p4().pt()",
          "slp_eta                             := Subleading_Photon.p4().eta()",
          "slp_SC_eta                          := Subleading_Photon.superCluster().eta()",
          "slp_phi                             := Subleading_Photon.p4().phi()",
          "slp_E                               := Subleading_Photon.p4().E()",
          "slp_initE                           := Subleading_Photon.energyAtStep('initial')",
          "slp_r9                              := Subleading_Photon.old_r9()",
          "slp_full5x5_r9                      := Subleading_Photon.full5x5_r9()",
          "slp_Hgg_MVA                         := slp_Hgg_MVA()",
          "slp_passElectronVeto                := Subleading_Photon.passElectronVeto()",
          "slp_hasPixelSeed                    := Subleading_Photon.hasPixelSeed",   

          # DiPhoton(s)
        #  "n_dipho                             := diphoVector.size()",
        #  "dipho_MVA                           := dipho_MVA()", 
        #  "CMS_hgg_mass                        := CMS_hgg_mass() ", # for cuts within HHWWggCandidate.cc before workspace 
       #   "leading_dpho_pt                     := ? leading_dpho.pt() != 0 ? leading_dpho.pt() : -99",
        #  "leading_dpho_eta                    := ? leading_dpho.eta() != 0 ? leading_dpho.eta() : -99",
         # "leading_dpho_phi                    := ? leading_dpho.phi() != 0 ? leading_dpho.phi() : -99",
         # "leading_dpho_E                      := ? leading_dpho.E() != 0 ? leading_dpho.E() : -99",

          # Electrons
          # If there is no leading electron (electronVector_.size() == 0) or no subleading electron (electronVector_.size() <= 1) plot -99 
          "leading_Electron_pt                     := Leading_Electron.pt() ",  
          "leading_Electron_eta                    := Leading_Electron.eta()",
          "leading_Electron_phi                    := Leading_Electron.phi()",
          "leading_Electron_E                      := Leading_Electron.E()",
          "subleading_Electron_pt                  := Subleading_Electron.pt()",
          "subleading_Electron_eta                 := Subleading_Electron.eta()",
          "subleading_Electron_phi                 := Subleading_Electron.phi()",
          "subleading_Electron_E                   := Subleading_Electron.E()",
          # If there is no leading muon (muonVector_.size() == 0) or no subleading muon (muonVector_.size() <= 1) plot -99 
          "leading_muon_pt                     := leading_muon.pt() ",
          "leading_muon_eta                    := leading_muon.eta() ",
          "leading_muon_phi                    := leading_muon.phi()",
          "leading_muon_E                      := leading_muon.E()",
          "subleading_muon_pt                  := subleading_muon.pt()",
          "subleading_muon_eta                 := subleading_muon.eta()",
          "subleading_muon_phi                 := subleading_muon.phi()",
          "subleading_muon_E                   := subleading_muon.E()",
          "Met_pt                              := MET.pt()"
        ]
        #variables += cutFlowVars 
        #variables += bScores 
        #variables += phoEs
        #variables += Reco_var
        return variables

        # if self.customize.dumpWorkspace == False :
        #     return variables
        # else :
        #     return var_workspace


    def systematicVariables(self):
    #   systematicVariables=["CMS_hgg_mass[160,100,180]:=diPhoton().mass","Mjj[120,70,190]:=dijet().M()","HHbbggMVA[100,0,1.]:=MVA()","MX[300,250,5000]:=MX()"]
      systematicVariables=[
        #   "dZ",
          "CMS_hgg_mass[160,100,180]:=diPhoton().mass"
        #   "lp_E[100,0,100] := Leading_Photon.p4().E()",
        #   "slp_E[100,0,100] := Subleading_Photon.p4().E()",
        #   "lp_initE[100,0,100] := Leading_Photon.energyAtStep('initial')",
        #   "slp_initE[100,0,100] := Subleading_Photon.energyAtStep('initial')", # also want final energies 
      ]

      return systematicVariables


    def variablesToDumpData():
        variables = [
            # "testVariable[100,0,100] := 50"
            # "jet0_btag[2,0,2]                       := ? JetVector.size() >= 1 ? JetVector[0].bDiscriminator('mini_pfDeepFlavourJetTags:probb') : -99 ",
            # "TestVariable:=111"
           #  "leadingJet_DeepCSV := leadJet().bDiscriminator('pfDeepCSVJetTags:probb')+leadJet().bDiscriminator('pfDeepCSVJetTags:probbb')",#FIXME make the btag type configurable?
           #  "subleadingJet_DeepCSV := subleadJet().bDiscriminator('pfDeepCSVJetTags:probb')+subleadJet().bDiscriminator('pfDeepCSVJetTags:probbb')",
           #  "absCosThetaStar_CS := abs(getCosThetaStar_CS())",
           #  "absCosThetaStar_CS_old := abs(getCosThetaStar_CS_old(6500))",
           #  "absCosTheta_bb := abs(CosThetaAngles()[1])",
           #  "absCosTheta_gg := abs(CosThetaAngles()[0])",
           #  "diphotonCandidatePtOverdiHiggsM := diphotonPtOverM()",
           #  "dijetCandidatePtOverdiHiggsM := dijetPtOverM()",
           #  "customLeadingPhotonIDMVA := diPhoton.leadingView.phoIdMvaWrtChosenVtx",
           #  "customSubLeadingPhotonIDMVA := diPhoton.subLeadingView.phoIdMvaWrtChosenVtx",
           #  "leadingPhotonSigOverE := diPhoton.leadingPhoton.sigEOverE",
           #  "subleadingPhotonSigOverE := diPhoton.subLeadingPhoton.sigEOverE",
           #  "sigmaMOverM := sqrt(0.5*(diPhoton.leadingPhoton.sigEOverE*diPhoton.leadingPhoton.sigEOverE + diPhoton.subLeadingPhoton.sigEOverE*diPhoton.subLeadingPhoton.sigEOverE))",
           #  "PhoJetMinDr := getPhoJetMinDr()",#up to here input variables to MVA
           #  "leadingJet_bRegNNResolution := leadJet().userFloat('bRegNNResolution')",
           #  "subleadingJet_bRegNNResolution := subleadJet().userFloat('bRegNNResolution')",
           #  "sigmaMJets := getSigmaMOverMJets()",
            #  "HHbbggMVA := MVA()",
            #  "MX := MX()",
           #  "Mjj := dijet().M()",
           #  "eventNumber := eventNumber()",
             ]

        # for jeti in range(0,6):
        #     var = "jet" + str(jeti) + "_btag[2,0,2] := ? JetVector.size() >= " + str(jeti + 1) + " ? JetVector[" + str(jeti) + "].bDiscriminator('mini_pfDeepFlavourJetTags:probb') : -99 "
        #     variables.append(var)

        # if self.customize.doHHWWggttHKiller : variables +=[
        #     "ttHScore := ttHScore()",
        #    ]
        return variables



    def customizeTagSequence(self):
        self.process.load("flashgg.Taggers.flashggHHWWggFLTag_cff")

        if self.customize.doHHWWggFLTagCutFlow:
            self.process.flashggHHWWggFLTag.doHHWWggFLTagCutFlowAnalysis = cms.bool(True)

        ## customize meta conditions
        # self.process.flashggHHWWggFLTag.JetIDLevel=cms.string(str(self.metaConditions["doubleHTag"]["jetID"]))
        # self.process.flashggHHWWggFLTag.MVAConfig.weights=cms.FileInPath(str(self.metaConditions["doubleHTag"]["weightsFile"]))  
        # self.process.flashggHHWWggFLTag.MVAscaling = cms.double(self.metaConditions["doubleHTag"]["MVAscalingValue"])
        # self.process.flashggHHWWggFLTag.MVAFlatteningFileName = cms.untracked.FileInPath(str(self.metaConditions["doubleHTag"]["MVAFlatteningFileName"]))
        # self.process.flashggHHWWggFLTag.dottHTagger = cms.bool(self.customize.doHHWWggttHKiller)
        # self.process.flashggHHWWggFLTag.ttHWeightfile = cms.untracked.FileInPath(str(self.metaConditions["doubleHTag"]["ttHWeightfile"]))
        # self.process.flashggHHWWggFLTag.ttHKiller_mean = cms.vdouble(self.metaConditions["doubleHTag"]["ttHKiller_mean"])
        # self.process.flashggHHWWggFLTag.ttHKiller_std = cms.vdouble(self.metaConditions["doubleHTag"]["ttHKiller_std"])
        # self.process.flashggHHWWggFLTag.ttHKiller_listmean = cms.vdouble(self.metaConditions["doubleHTag"]["ttHKiller_listmean"])
        # self.process.flashggHHWWggFLTag.ttHKiller_liststd = cms.vdouble(self.metaConditions["doubleHTag"]["ttHKiller_liststd"])

        ## remove single Higgs tags

        print'Removing single Higgs tags'

        if self.customize.HHWWggFLTagsOnly:
            self.process.flashggTagSequence.remove(self.process.flashggVBFTag)
            self.process.flashggTagSequence.remove(self.process.flashggTTHLeptonicTag)
            self.process.flashggTagSequence.remove(self.process.flashggTTHHadronicTag)
            self.process.flashggTagSequence.remove(self.process.flashggVHEtTag)
            self.process.flashggTagSequence.remove(self.process.flashggVHLooseTag)
            self.process.flashggTagSequence.remove(self.process.flashggVHTightTag)
            self.process.flashggTagSequence.remove(self.process.flashggVHMetTag)
            self.process.flashggTagSequence.remove(self.process.flashggWHLeptonicTag)
            self.process.flashggTagSequence.remove(self.process.flashggZHLeptonicTag)
            self.process.flashggTagSequence.remove(self.process.flashggVHLeptonicLooseTag)
            self.process.flashggTagSequence.remove(self.process.flashggVHHadronicTag)
            self.process.flashggTagSequence.remove(self.process.flashggVBFMVA)
            self.process.flashggTagSequence.remove(self.process.flashggVBFDiPhoDiJetMVA)
            self.process.flashggTagSequence.remove(self.process.flashggTTHDiLeptonTag)
            self.process.flashggTagSequence.remove(self.process.flashggUntagged)
            self.process.flashggTagSequence.remove(self.process.flashggUntagged)
            self.process.flashggTagSequence.remove(self.process.flashggTHQLeptonicTag)

        self.process.flashggTagSequence.replace(self.process.flashggTagSorter,self.process.flashggHHWWggFLTagSequence*self.process.flashggTagSorter)
        self.process.flashggTagSorter.TagPriorityRanges = cms.VPSet( cms.PSet(TagName = cms.InputTag('flashggHHWWggFLTag')) )
 
    def HHWWggFLTagMerger(self,systlabels=[]):
        self.process.p.remove(self.process.flashggTagSorter)
        self.process.p.replace(self.process.flashggSystTagMerger,self.process.flashggHHWWggFLTagSequence*self.process.flashggTagSorter*self.process.flashggSystTagMerger)
        # print'process.p = ',self.process.p 
        
        ##-- Do I need this part for HHWWgg?
        for systlabel in systlabels:
           if systlabel!='':
             self.process.p.remove(getattr(self.process,'flashggTagSorter'+systlabel))
             self.process.p.replace(self.process.flashggSystTagMerger,getattr(self.process, 'flashggTagSorter'+systlabel)*self.process.flashggSystTagMerger)
           setattr(getattr(self.process, 'flashggTagSorter'+systlabel), 'TagPriorityRanges', cms.VPSet( cms.PSet(TagName = cms.InputTag('flashggHHWWggFLTag')) ))
        #    setattr(getattr(self.process, 'flashggTagSorter'+systlabel), 'TagPriorityRanges', cms.VPSet( cms.PSet(TagName = cms.InputTag('flashggHHWWggFLTag', systlabel)) ))
        
        # print 'from loop after:',process.flashggSystTagMerger.src


    def HHWWggFLTagRunSequence(self,systlabels,jetsystlabels,phosystlabels):
        print'not used'
    #    if self.customize.HHWWggFLTagsOnly: 
        #   print'systlabels = ',systlabels 
        #   self.HHWWggFLTagMerger(systlabels)


        ## Not sure if this is necessary for HHWWgg
    #    if len(systlabels)>1 :
    #       print'[HHWWggFLTagRunSequence] - Add JetesSuffixes and diphotonsuffices' 
    #       getattr(self.process, "flashggHHWWggFLTag").JetsSuffixes = cms.vstring([systlabels[0]]+jetsystlabels)
    #       getattr(self.process, "flashggHHWWggFLTag").DiPhotonSuffixes = cms.vstring([systlabels[0]]+phosystlabels)





    #    if self.customize.HHWWggReweight>0:
        #   self.addNodesReweighting()
    
    #    if self.customize.doHHWWggGenAnalysis:
        #   self.addGenAnalysis()



    def addNodesReweighting(self):
        print'[addNodesReweighting]: Doing Nothing for HHWWgg'
        # if self.customize.HHWWggReweight > 0 :
        #     from flashgg.Taggers.flashggHHWWggReweight_cfi import flashggHHWWggReweight
        #     self.process.flashggHHWWggReweight = flashggHHWWggReweight
        #     self.process.flashggHHWWggReweight.doReweight = self.customize.HHWWggReweight
        #     self.process.flashggHHWWggReweight.weightsFile = cms.untracked.FileInPath(str(self.metaConditions["HHWWggFLTag"]["NodesReweightingFileName"]))
        #     self.process.p.replace(self.process.flashggHHWWggFLTag, self.process.flashggHHWWggReweight*self.process.flashggHHWWggFLTag)


    def addGenAnalysis(self):
        if self.customize.processId == "Data": 
            return 

        import flashgg.Taggers.dumperConfigTools as cfgTools
        ## load gen-level bbgg 
        self.process.load( "flashgg.MicroAOD.flashggGenDiPhotonDiBJetsSequence_cff" )

        ## match gen-level to reco tag
        self.process.load("flashgg.Taggers.flashggTaggedGenDiphotons_cfi")
        self.process.flashggTaggedGenDiphotons.src  = "flashggSelectedGenDiPhotonDiBJets"
        self.process.flashggTaggedGenDiphotons.tags = "flashggTagSorter"
        self.process.flashggTaggedGenDiphotons.remap = self.process.tagsDumper.classifierCfg.remap

        ## prepare gen-level dumper
        self.process.load("flashgg.Taggers.genDiphotonDumper_cfi")
        self.process.genDiphotonDumper.dumpTrees = True
        self.process.genDiphotonDumper.dumpWorkspace = False
        self.process.genDiphotonDumper.src = "flashggTaggedGenDiphotons"

        from flashgg.Taggers.globalVariables_cff import globalVariables
        self.process.genDiphotonDumper.dumpGlobalVariables = True
        self.process.genDiphotonDumper.globalVariables = globalVariables

        genVariables = ["mgg := mass",
                        "mbb := dijet.mass",
                        "mhh := sqrt( pow(energy+dijet.energy,2) - pow(px+dijet.px,2) - pow(py+dijet.py,2) - pow(pz+dijet.pz,2))",                    


                        "leadPho_px := leadingPhoton.px",
                        "leadPho_py := leadingPhoton.py",
                        "leadPho_pz := leadingPhoton.pz",
                        "leadPho_e  := leadingPhoton.energy",
                        "subleadPho_px := subLeadingPhoton.px",
                        "subleadPho_py := subLeadingPhoton.py",
                        "subleadPho_pz := subLeadingPhoton.pz",
                        "subleadPho_e  := subLeadingPhoton.energy",

                        "leadJet_px := leadingJet.px",
                        "leadJet_py := leadingJet.py",
                        "leadJet_pz := leadingJet.pz",
                        "leadJet_e  := leadingJet.energy",
                        "subleadJet_px := subLeadingJet.px",
                        "subleadJet_py := subLeadingJet.py",
                        "subleadJet_pz := subLeadingJet.pz",
                        "subleadJet_e  := subLeadingJet.energy",

                        ]
        # if self.customize.HHWWggReweight > 0: 
        #      for num in range(0,12):
        #            genVariables += ["benchmark_reweight_%d := getHHbbggBenchmarkReweight(%d)"%(num,num)]
        #      genVariables += ["benchmark_reweight_SM := getHHbbggBenchmarkReweight(12)"]
        #      genVariables += ["benchmark_reweight_box := getHHbbggBenchmarkReweight(13)"]
        #      genVariables += ["benchmark_reweight_2017fake := getHHbbggBenchmarkReweight(14)"]

        ## define categories for gen-level dumper
        cfgTools.addCategory(self.process.genDiphotonDumper,  ## events with not reco-level tag
                             "NoTag", 'isTagged("flashggNoTag")',1,
                             variables=genVariables,
                             )

        for tag in self.tagList: ## tagged events
            tagName,subCats = tag
            # need to define all categories explicitely because cut-based classifiers do not look at sub-category number
            for isub in xrange(subCats):
                cfgTools.addCategory(self.process.genDiphotonDumper,
                                     "%s_%d" % ( tagName, isub ), 
                                     'isTagged("%s") && categoryNumber == %d' % (tagName, isub),0,
                                     variables=genVariables##+recoVariables
                                     )

        self.process.genp = cms.Path(self.process.flashggGenDiPhotonDiBJetsSequence*self.process.flashggTaggedGenDiphotons*self.process.genDiphotonDumper)
