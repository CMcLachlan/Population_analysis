# POPULATION ANALYSIS PYTHON SCRIPT - ANALYSIS OF CENSUS AND IMD DATA FOR A DEFINED AREA

# ---------------------------------------------------------------------------------------------------------------------
# IMPORTS
import pandas as pd

# ---------------------------------------------------------------------------------------------------------------------
# READ DATA FILES

Car_van = pd.read_csv(
    r'C:/Users/charl/Documents/Essex Wildlife Trust/Population analysis private/census2021-ts045-lsoa.csv')

Dwellings = pd.read_csv(
    r'C:/Users/charl/Documents/Essex Wildlife Trust/Population analysis private/census2021-ts044-lsoaDwellingType.csv')

Economic = pd.read_csv(
    r'C:/Users/charl/Documents/Essex Wildlife Trust/Population analysis private/census2021-ts066-lsoaEconomicActivity'
    r'.csv')

DeprivationDimensions = pd.read_csv(
    r'C:/Users/charl/Documents/Essex Wildlife Trust/Population analysis private/census2021-ts011-lsoaDeprivation'
    r'Dimensions.csv')

HighestEd = pd.read_csv(
    r'C:/Users/charl/Documents/Essex Wildlife Trust/Population analysis private/census2021-ts067-lsoaHighestEd.csv')

Ethnicity = pd.read_csv(
    r'C:/Users/charl/Documents/Essex Wildlife Trust/Population analysis private/census2021-ts021-lsoaEthnicity.csv')

Health = pd.read_csv(
    r'C:/Users/charl/Documents/Essex Wildlife Trust/Population analysis private/census2021-ts037-lsoaHealth.csv')

Disability = pd.read_csv(
    r'C:/Users/charl/Documents/Essex Wildlife Trust/Population analysis private/census2021-ts038-lsoaDisability.csv')

UnpaidCare = pd.read_csv(
    r'C:/Users/charl/Documents/Essex Wildlife Trust/Population analysis private/census2021-ts039-lsoaUnpaidCare.csv')

HoursWorked = pd.read_csv(
    r'C:/Users/charl/Documents/Essex Wildlife Trust/Population analysis private/census2021-ts059-lsoaHoursWorked.csv')

HouseholdComposition = pd.read_csv(
    r'C:/Users/charl/Documents/Essex Wildlife Trust/Population analysis private/census2021-ts003-lsoaHousehold'
    r'Composition.csv')

Occupation = pd.read_csv(
    r'C:/Users/charl/Documents/Essex Wildlife Trust/Population analysis private/census2021-ts063-lsoaOccupation.csv')

LegalPartnership = pd.read_csv(
    r'C:/Users/charl/Documents/Essex Wildlife Trust/Population analysis private/census2021-ts002-'
    r'lsoaLegalPartnership.csv')

HouseholdLanguage = pd.read_csv(
    r'C:/Users/charl/Documents/Essex Wildlife Trust/Population analysis private/census2021-ts025-lsoaLanguage.csv')

NSEC = pd.read_csv(
    r'C:/Users/charl/Documents/Essex Wildlife Trust/Population analysis private/census2021-ts062-lsoaNS-SeC.csv')

Religion = pd.read_csv(
    r'C:/Users/charl/Documents/Essex Wildlife Trust/Population analysis private/census2021-ts030-lsoaReligion.csv')

Tenure = pd.read_csv(
    r'C:/Users/charl/Documents/Essex Wildlife Trust/Population analysis private/census2021-ts054-lsoaTenure.csv')

IMD = pd.read_csv(
    r'C:/Users/charl/Documents/Essex Wildlife Trust/Population analysis private/File_7_-_All_IoD2019_Scores__Ranks'
    r'__Deciles_and_Population_Denominators_3.csv')

# ---------------------------------------------------------------------------------------------------------------------
# ARCPRO EXTRACTED ROWS TO BE USED IN FILTERING DATA TO APPROPRIATE AREAS
ProjLSOA = pd.read_csv(
    r'C:/Users/charl/Documents/Essex Wildlife Trust/Population analysis private/ProjLSOAs.csv')
BuffLSOA = pd.read_csv(
    r'C:/Users/charl/Documents/Essex Wildlife Trust/Population analysis private/BuffLSOAs.csv')
Buff2LSOA = pd.read_csv(
    r'C:/Users/charl/Documents/Essex Wildlife Trust/Population analysis private/Buff8LSOAs.csv')

# ---------------------------------------------------------------------------------------------------------------------
# DEFINE FUNCTIONS
def census_stats(data, proj, resultfile, section, all, v1, t1, v2, t2, v3, t3, v4, t4, v5=None, t5=None, v6=None,
                 t6=None, v7=None, t7=None, v8=None, t8=None, v9=None, t9=None, v10=None, t10=None, v11=None, t11=None,
                 v12=None, t12=None, v13=None, t13=None, v14=None, t14=None, v15=None, t15=None, v16=None, t16=None,
                 v17=None, t17=None, v18=None, t18=None, v19=None, t19=None, v20=None, t20=None):
    """
    Given a dataset containing up to 20 variables, a dataframe of LSOAs based on a project area and a dataframe of LSOAs
    based on a buffer area, calculate percentages for each variable for each area, calculate the relative ratio of
    the percentages compared to the national dataset, and write (append) the results to a text file.
    :param data: dataframe
        Dataframe containing the national dataset
    :param proj: dataframe
        Dataframe containing the LSOAs for the project area
    :param resultfile: text file
        Text file for the results to be written to
    :param section: text
        Title for the section of text to be added
    :param all: data column
        Name of column within "data" containing the totals for the dataset
    :param v1-20: variable column names
    :param t1-20: text to be used in output relating to the variables defined
    :return: updated results
        Text to be added to the results file
    """

    # ALL DATA PERCENTAGES
    TotalAll = data['{}'.format(all)].sum()
    if v1:
        Totalv1 = data['{}'.format(v1)].sum()
    if v2:
        Totalv2 = data['{}'.format(v2)].sum()
    if v3:
        Totalv3 = data['{}'.format(v3)].sum()
    if v4:
        Totalv4 = data['{}'.format(v4)].sum()
    if v5:
        Totalv5 = data['{}'.format(v5)].sum()
    if v6:
        Totalv6 = data['{}'.format(v6)].sum()
    if v7:
        Totalv7 = data['{}'.format(v7)].sum()
    if v8:
        Totalv8 = data['{}'.format(v8)].sum()
    if v9:
        Totalv9 = data['{}'.format(v9)].sum()
    if v10:
        Totalv10 = data['{}'.format(v10)].sum()
    if v11:
        Totalv11 = data['{}'.format(v11)].sum()
    if v12:
        Totalv12 = data['{}'.format(v12)].sum()
    if v13:
        Totalv13 = data['{}'.format(v13)].sum()
    if v14:
        Totalv14 = data['{}'.format(v14)].sum()
    if v15:
        Totalv15 = data['{}'.format(v15)].sum()
    if v16:
        Totalv16 = data['{}'.format(v16)].sum()
    if v17:
        Totalv17 = data['{}'.format(v17)].sum()
    if v18:
        Totalv18 = data['{}'.format(v18)].sum()
    if v19:
        Totalv19 = data['{}'.format(v19)].sum()
    if v20:
        Totalv20 = data['{}'.format(v20)].sum()

    if v1:
        PerTotalv1 = (Totalv1 / TotalAll) * 100
    if v2:
        PerTotalv2 = (Totalv2 / TotalAll) * 100
    if v3:
        PerTotalv3 = (Totalv3 / TotalAll) * 100
    if v4:
        PerTotalv4 = (Totalv4 / TotalAll) * 100
    if v5:
        PerTotalv5 = (Totalv5 / TotalAll) * 100
    if v6:
        PerTotalv6 = (Totalv6 / TotalAll) * 100
    if v7:
        PerTotalv7 = (Totalv7 / TotalAll) * 100
    if v8:
        PerTotalv8 = (Totalv8 / TotalAll) * 100
    if v9:
        PerTotalv9 = (Totalv9 / TotalAll) * 100
    if v10:
        PerTotalv10 = (Totalv10 / TotalAll) * 100
    if v11:
        PerTotalv11 = (Totalv11 / TotalAll) * 100
    if v12:
        PerTotalv12 = (Totalv12 / TotalAll) * 100
    if v13:
        PerTotalv13 = (Totalv13 / TotalAll) * 100
    if v14:
        PerTotalv14 = (Totalv14 / TotalAll) * 100
    if v15:
        PerTotalv15 = (Totalv15 / TotalAll) * 100
    if v16:
        PerTotalv16 = (Totalv16 / TotalAll) * 100
    if v17:
        PerTotalv17 = (Totalv17 / TotalAll) * 100
    if v18:
        PerTotalv18 = (Totalv18 / TotalAll) * 100
    if v19:
        PerTotalv19 = (Totalv19 / TotalAll) * 100
    if v20:
        PerTotalv20 = (Totalv20 / TotalAll) * 100

    # FILTER TO PROJECT AREA
    ProjData = proj.join(data.set_index('geography code'), on='LSOA21CD', how='left',
                               validate='one_to_one')

    # PROJECT AREA PERCENTAGES AND RATIOS
    ProjAll = ProjData['{}'.format(all)].sum()
    if v1:
        Projv1 = ProjData['{}'.format(v1)].sum()
    if v2:
        Projv2 = ProjData['{}'.format(v2)].sum()
    if v3:
        Projv3 = ProjData['{}'.format(v3)].sum()
    if v4:
        Projv4 = ProjData['{}'.format(v4)].sum()
    if v5:
        Projv5 = ProjData['{}'.format(v5)].sum()
    if v6:
        Projv6 = ProjData['{}'.format(v6)].sum()
    if v7:
        Projv7 = ProjData['{}'.format(v7)].sum()
    if v8:
        Projv8 = ProjData['{}'.format(v8)].sum()
    if v9:
        Projv9 = ProjData['{}'.format(v9)].sum()
    if v10:
        Projv10 = ProjData['{}'.format(v10)].sum()
    if v11:
        Projv11 = ProjData['{}'.format(v11)].sum()
    if v12:
        Projv12 = ProjData['{}'.format(v12)].sum()
    if v13:
        Projv13 = ProjData['{}'.format(v13)].sum()
    if v14:
        Projv14 = ProjData['{}'.format(v14)].sum()
    if v15:
        Projv15 = ProjData['{}'.format(v15)].sum()
    if v16:
        Projv16 = ProjData['{}'.format(v16)].sum()
    if v17:
        Projv17 = ProjData['{}'.format(v17)].sum()
    if v18:
        Projv18 = ProjData['{}'.format(v18)].sum()
    if v19:
        Projv19 = ProjData['{}'.format(v19)].sum()
    if v20:
        Projv20 = ProjData['{}'.format(v20)].sum()

    if v1:
        PerProjv1 = (Projv1 / ProjAll) * 100
    if v2:
        PerProjv2 = (Projv2 / ProjAll) * 100
    if v3:
        PerProjv3 = (Projv3 / ProjAll) * 100
    if v4:
        PerProjv4 = (Projv4 / ProjAll) * 100
    if v5:
        PerProjv5 = (Projv5 / ProjAll) * 100
    if v6:
        PerProjv6 = (Projv6 / ProjAll) * 100
    if v7:
        PerProjv7 = (Projv7 / ProjAll) * 100
    if v8:
        PerProjv8 = (Projv8 / ProjAll) * 100
    if v9:
        PerProjv9 = (Projv9 / ProjAll) * 100
    if v10:
        PerProjv10 = (Projv10 / ProjAll) * 100
    if v11:
        PerProjv11 = (Projv11 / ProjAll) * 100
    if v12:
        PerProjv12 = (Projv12 / ProjAll) * 100
    if v13:
        PerProjv13 = (Projv13 / ProjAll) * 100
    if v14:
        PerProjv14 = (Projv14 / ProjAll) * 100
    if v15:
        PerProjv15 = (Projv15 / ProjAll) * 100
    if v16:
        PerProjv16 = (Projv16 / ProjAll) * 100
    if v17:
        PerProjv17 = (Projv17 / ProjAll) * 100
    if v18:
        PerProjv18 = (Projv18 / ProjAll) * 100
    if v19:
        PerProjv19 = (Projv19 / ProjAll) * 100
    if v20:
        PerProjv20 = (Projv20 / ProjAll) * 100

    if v1:
        RatioProjv1 = PerProjv1 / PerTotalv1
    if v2:
        RatioProjv2 = PerProjv2 / PerTotalv2
    if v3:
        RatioProjv3 = PerProjv3 / PerTotalv3
    if v4:
        RatioProjv4 = PerProjv4 / PerTotalv4
    if v5:
        RatioProjv5 = PerProjv5 / PerTotalv5
    if v6:
        RatioProjv6 = PerProjv6 / PerTotalv6
    if v7:
        RatioProjv7 = PerProjv7 / PerTotalv7
    if v8:
        RatioProjv8 = PerProjv8 / PerTotalv8
    if v9:
        RatioProjv9 = PerProjv9 / PerTotalv9
    if v10:
        RatioProjv10 = PerProjv10 / PerTotalv10
    if v11:
        RatioProjv11 = PerProjv11 / PerTotalv11
    if v12:
        RatioProjv12 = PerProjv12 / PerTotalv12
    if v13:
        RatioProjv13 = PerProjv13 / PerTotalv13
    if v14:
        RatioProjv14 = PerProjv14 / PerTotalv14
    if v15:
        RatioProjv15 = PerProjv15 / PerTotalv15
    if v16:
        RatioProjv16 = PerProjv16 / PerTotalv16
    if v17:
        RatioProjv17 = PerProjv17 / PerTotalv17
    if v18:
        RatioProjv18 = PerProjv18 / PerTotalv18
    if v19:
        RatioProjv19 = PerProjv19 / PerTotalv19
    if v20:
        RatioProjv20 = PerProjv20 / PerTotalv20

    # WRITE RESULTS TO FILE
    updatedresults = open(resultfile, "a")
    updatedresults.write('\n{} \n'.format(section))
    if t1:
        updatedresults.write('{}: {:.2f}%, {:.2f} times the national percentage. \n'.format(t1, PerProjv1, RatioProjv1))
    if t2:
        updatedresults.write('{}: {:.2f}%, {:.2f} times the national percentage. \n'.format(t2, PerProjv2, RatioProjv2))
    if t3:
        updatedresults.write('{}: {:.2f}%, {:.2f} times the national percentage. \n'.format(t3, PerProjv3, RatioProjv3))
    if t4:
        updatedresults.write('{}: {:.2f}%, {:.2f} times the national percentage. \n'.format(t4, PerProjv4, RatioProjv4))
    if t5:
        updatedresults.write('{}: {:.2f}%, {:.2f} times the national percentage. \n'.format(t5, PerProjv5, RatioProjv5))
    if t6:
        updatedresults.write('{}: {:.2f}%, {:.2f} times the national percentage. \n'.format(t6, PerProjv6, RatioProjv6))
    if t7:
        updatedresults.write('{}: {:.2f}%, {:.2f} times the national percentage. \n'.format(t7, PerProjv7, RatioProjv7))
    if t8:
        updatedresults.write('{}: {:.2f}%, {:.2f} times the national percentage. \n'.format(t8, PerProjv8, RatioProjv8))
    if t9:
        updatedresults.write('{}: {:.2f}%, {:.2f} times the national percentage. \n'.format(t9, PerProjv9, RatioProjv9))
    if t10:
        updatedresults.write('{}: {:.2f}%, {:.2f} times the national percentage. \n'.format(t10, PerProjv10,
                                                                                            RatioProjv10))
    if t11:
        updatedresults.write('{}: {:.2f}%, {:.2f} times the national percentage. \n'.format(t11, PerProjv11,
                                                                                            RatioProjv11))
    if t12:
        updatedresults.write('{}: {:.2f}%, {:.2f} times the national percentage. \n'.format(t12, PerProjv12,
                                                                                            RatioProjv12))
    if t13:
        updatedresults.write('{}: {:.2f}%, {:.2f} times the national percentage. \n'.format(t13, PerProjv13,
                                                                                            RatioProjv13))
    if t14:
        updatedresults.write('{}: {:.2f}%, {:.2f} times the national percentage. \n'.format(t14, PerProjv14,
                                                                                            RatioProjv14))
    if t15:
        updatedresults.write('{}: {:.2f}%, {:.2f} times the national percentage. \n'.format(t15, PerProjv15,
                                                                                            RatioProjv15))
    if t16:
        updatedresults.write('{}: {:.2f}%, {:.2f} times the national percentage. \n'.format(t16, PerProjv16,
                                                                                            RatioProjv16))
    if t17:
        updatedresults.write('{}: {:.2f}%, {:.2f} times the national percentage. \n'.format(t17, PerProjv17,
                                                                                            RatioProjv17))
    if t18:
        updatedresults.write('{}: {:.2f}%, {:.2f} times the national percentage. \n'.format(t18, PerProjv18,
                                                                                            RatioProjv18))
    if t19:
        updatedresults.write('{}: {:.2f}%, {:.2f} times the national percentage. \n'.format(t19, PerProjv19,
                                                                                            RatioProjv19))
    if t20:
        updatedresults.write('{}: {:.2f}%, {:.2f} times the national percentage. \n'.format(t20, PerProjv20,
                                                                                            RatioProjv20))
    updatedresults.close()
    results = updatedresults
    return results


def IMD_stats(data, proj, buffer1, buffer2, alltotal, v1, t1, v2, t2, v3, t3, v4, t4, v5=None, t5=None, v6=None,
              t6=None, v7=None, t7=None, v8=None, t8=None, v9=None, t9=None, v10=None, t10=None, v11=None, t11=None,
              v12=None, t12=None, v13=None, t13=None, v14=None, t14=None, v15=None, t15=None, v16=None, t16=None,
              v17=None, t17=None, v18=None, t18=None, v19=None, t19=None, v20=None, t20=None):
    """
    Given a dataset containing up to 20 variables, a dataframe of LSOAs based on a project area and a dataframe of LSOAs
    based on a buffer area, calculate average IMD deciles for the defined area.
    :param data: dataframe
        Dataframe containing the national dataset
    :param proj: dataframe
        Dataframe containing the LSOAs for the project area
    :param buffer1: dataframe
        Dataframe containing the LSOAs for the buffer area
    :param buffer2: dataframe
        Dataframe containing the LSOAs for the second buffer area
    :param alltotal: data column
        Name of column within "data" containing the totals for the dataset
    :param v1-20: variable column names
    :param t1-20: text to be used in column heading output relating to the variables defined
    :return: average deciles
        dataframe containing averages calculated
    """

    # FILTER TO PROJECT AREA
    ProjData = proj.join(data.set_index('LSOA code (2011)'), on='LSOA21CD', how='left',
                               validate='one_to_one')

    # ALL DATA AVERAGES
    Sum1 = {'Area name': ['Project area']}
    Summary = pd.DataFrame(Sum1)
    Summary['Mean IMD Decile'] = ProjData['{}'.format(alltotal)].mean()
    if v1:
        Summary['{}'.format(t1)] = ProjData['{}'.format(v1)].mean()
    if v2:
        Summary['{}'.format(t2)] = ProjData['{}'.format(v2)].mean()
    if v3:
        Summary['{}'.format(t3)] = ProjData['{}'.format(v3)].mean()
    if v4:
        Summary['{}'.format(t4)] = ProjData['{}'.format(v4)].mean()
    if v5:
        Summary['{}'.format(t5)] = ProjData['{}'.format(v5)].mean()
    if v6:
        Summary['{}'.format(t6)] = ProjData['{}'.format(v6)].mean()
    if v7:
        Summary['{}'.format(t7)] = ProjData['{}'.format(v7)].mean()
    if v8:
        Summary['{}'.format(t8)] = ProjData['{}'.format(v8)].mean()
    if v9:
        Summary['{}'.format(t9)] = ProjData['{}'.format(v9)].mean()
    if v10:
        Summary['{}'.format(t10)] = ProjData['{}'.format(v10)].mean()
    if v11:
        Summary['{}'.format(t11)] = ProjData['{}'.format(v11)].mean()
    if v12:
        Summary['{}'.format(t12)] = ProjData['{}'.format(v12)].mean()
    if v13:
        Summary['{}'.format(t13)] = ProjData['{}'.format(v13)].mean()
    if v14:
        Summary['{}'.format(t14)] = ProjData['{}'.format(v14)].mean()
    if v15:
        Summary['{}'.format(t15)] = ProjData['{}'.format(v15)].mean()
    if v16:
        Summary['{}'.format(t16)] = ProjData['{}'.format(v16)].mean()
    if v17:
        Summary['{}'.format(t17)] = ProjData['{}'.format(v17)].mean()
    if v18:
        Summary['{}'.format(t18)] = ProjData['{}'.format(v18)].mean()
    if v19:
        Summary['{}'.format(t19)] = ProjData['{}'.format(v19)].mean()
    if v20:
        Summary['{}'.format(t20)] = ProjData['{}'.format(v20)].mean()

    # FILTER TO BUFFER AREA
    BuffData = buffer1.join(data.set_index('LSOA code (2011)'), on='LSOA21CD', how='left',
                               validate='one_to_one')

    # PROJECT AREA PERCENTAGES AND RATIOS
    Buff1 = {'Area name': ['4 mile buffer']}
    BuffSummary = pd.DataFrame(Buff1)
    BuffSummary['Mean IMD Decile'] = BuffData['{}'.format(alltotal)].mean()
    if v1:
        BuffSummary['{}'.format(t1)] = BuffData['{}'.format(v1)].mean()
    if v2:
        BuffSummary['{}'.format(t2)] = BuffData['{}'.format(v2)].mean()
    if v3:
        BuffSummary['{}'.format(t3)] = BuffData['{}'.format(v3)].mean()
    if v4:
        BuffSummary['{}'.format(t4)] = BuffData['{}'.format(v4)].mean()
    if v5:
        BuffSummary['{}'.format(t5)] = BuffData['{}'.format(v5)].mean()
    if v6:
        BuffSummary['{}'.format(t6)] = BuffData['{}'.format(v6)].mean()
    if v7:
        BuffSummary['{}'.format(t7)] = BuffData['{}'.format(v7)].mean()
    if v8:
        BuffSummary['{}'.format(t8)] = BuffData['{}'.format(v8)].mean()
    if v9:
        BuffSummary['{}'.format(t9)] = BuffData['{}'.format(v9)].mean()
    if v10:
        BuffSummary['{}'.format(t10)] = BuffData['{}'.format(v10)].mean()
    if v11:
        BuffSummary['{}'.format(t11)] = BuffData['{}'.format(v11)].mean()
    if v12:
        BuffSummary['{}'.format(t12)] = BuffData['{}'.format(v12)].mean()
    if v13:
        BuffSummary['{}'.format(t13)] = BuffData['{}'.format(v13)].mean()
    if v14:
        BuffSummary['{}'.format(t14)] = BuffData['{}'.format(v14)].mean()
    if v15:
        BuffSummary['{}'.format(t15)] = BuffData['{}'.format(v15)].mean()
    if v16:
        BuffSummary['{}'.format(t16)] = BuffData['{}'.format(v16)].mean()
    if v17:
        BuffSummary['{}'.format(t17)] = BuffData['{}'.format(v17)].mean()
    if v18:
        BuffSummary['{}'.format(t18)] = BuffData['{}'.format(v18)].mean()
    if v19:
        BuffSummary['{}'.format(t19)] = BuffData['{}'.format(v19)].mean()
    if v20:
        BuffSummary['{}'.format(t20)] = BuffData['{}'.format(v20)].mean()

        # FILTER TO SECOND BUFFER AREA
    Buff2Data = buffer2.join(data.set_index('LSOA code (2011)'), on='LSOA21CD', how='left',
                            validate='one_to_one')

    # PROJECT AREA PERCENTAGES AND RATIOS
    Buff2 = {'Area name': ['8 mile buffer']}
    Buff2Summary = pd.DataFrame(Buff2)
    Buff2Summary['Mean IMD Decile'] = Buff2Data['{}'.format(alltotal)].mean()
    if v1:
        Buff2Summary['{}'.format(t1)] = Buff2Data['{}'.format(v1)].mean()
    if v2:
        Buff2Summary['{}'.format(t2)] = Buff2Data['{}'.format(v2)].mean()
    if v3:
        Buff2Summary['{}'.format(t3)] = Buff2Data['{}'.format(v3)].mean()
    if v4:
        Buff2Summary['{}'.format(t4)] = Buff2Data['{}'.format(v4)].mean()
    if v5:
        Buff2Summary['{}'.format(t5)] = Buff2Data['{}'.format(v5)].mean()
    if v6:
        Buff2Summary['{}'.format(t6)] = Buff2Data['{}'.format(v6)].mean()
    if v7:
        Buff2Summary['{}'.format(t7)] = Buff2Data['{}'.format(v7)].mean()
    if v8:
        Buff2Summary['{}'.format(t8)] = Buff2Data['{}'.format(v8)].mean()
    if v9:
        Buff2Summary['{}'.format(t9)] = Buff2Data['{}'.format(v9)].mean()
    if v10:
        Buff2Summary['{}'.format(t10)] = Buff2Data['{}'.format(v10)].mean()
    if v11:
        Buff2Summary['{}'.format(t11)] = Buff2Data['{}'.format(v11)].mean()
    if v12:
        Buff2Summary['{}'.format(t12)] = Buff2Data['{}'.format(v12)].mean()
    if v13:
        Buff2Summary['{}'.format(t13)] = Buff2Data['{}'.format(v13)].mean()
    if v14:
        Buff2Summary['{}'.format(t14)] = Buff2Data['{}'.format(v14)].mean()
    if v15:
        Buff2Summary['{}'.format(t15)] = Buff2Data['{}'.format(v15)].mean()
    if v16:
        Buff2Summary['{}'.format(t16)] = Buff2Data['{}'.format(v16)].mean()
    if v17:
        Buff2Summary['{}'.format(t17)] = Buff2Data['{}'.format(v17)].mean()
    if v18:
        Buff2Summary['{}'.format(t18)] = Buff2Data['{}'.format(v18)].mean()
    if v19:
        Buff2Summary['{}'.format(t19)] = Buff2Data['{}'.format(v19)].mean()
    if v20:
        Buff2Summary['{}'.format(t20)] = Buff2Data['{}'.format(v20)].mean()

    IMDResults = pd.concat([Summary, BuffSummary, Buff2Summary], ignore_index=True)
    return IMDResults


# ---------------------------------------------------------------------------------------------------------------------
# APPLY FUNCTION TO DATASETS

# RESULTS FILE DEFINITION
resultsfile = r'C:/Users/charl/Documents/Essex Wildlife Trust/Population analysis private/results.txt'

result = open(resultsfile, "w")
result.write('These results have been calculated from 2021 Census data from Nomis - provided by Office for National '
             'Statistics  (https://www.nomisweb.co.uk/census/2021/bulk). \nData has been filtered by Lower Super '
             'Output Area (LSOA). "Project area" refers to the LSOAs which have their centre within the project '
             'boundary. "4 mile buffer" refers to the LSOAs which have their centre between 0 and 4 miles outside '
             'the project boundary. "8 mile buffer" refers to the LSOAs which have their centre between 0 and 8 miles '
             'outside the project boundary. This ensures that, where an LSOA is intersected by the project boundary '
             'or buffer boundary, it is only analysed once - within the zone that the majority of its area falls '
             'within. \n')
result.close()

# CAR AND VAN AVAILABILITY
census_stats(Car_van, ProjLSOA, resultsfile, 'Car and van availability in the project area',
             'Number of cars or vans: Total: All households', 'Number of cars or vans: No cars or vans in household',
             'Percentage of households without a car or van in the project area',
             'Number of cars or vans: 1 car or van in household', 'Percentage of households with one car or van in the '
             'project area', 'Number of cars or vans: 2 cars or vans in household', 'Percentage of households with two '
             'cars or vans in the project area','Number of cars or vans: 3 or more cars or vans in household',
             'Percentage of households with three or more cars of vans in the project area')

census_stats(Car_van, BuffLSOA, resultsfile, 'Car and van availability in the 4 mile buffer area',
             'Number of cars or vans: Total: All households', 'Number of cars or vans: No cars or vans in household',
             'Percentage of households without a car or van in the buffer area',
             'Number of cars or vans: 1 car or van in household', 'Percentage of households with one car or van in the '
             'buffer area', 'Number of cars or vans: 2 cars or vans in household', 'Percentage of households with two '
             'cars or vans in the buffer area','Number of cars or vans: 3 or more cars or vans in household',
             'Percentage of households with three or more cars of vans in the buffer area')

census_stats(Car_van, Buff2LSOA, resultsfile, 'Car and van availability in the 8 mile buffer area',
             'Number of cars or vans: Total: All households', 'Number of cars or vans: No cars or vans in household',
             'Percentage of households without a car or van in the buffer area',
             'Number of cars or vans: 1 car or van in household', 'Percentage of households with one car or van in the '
             'buffer area', 'Number of cars or vans: 2 cars or vans in household', 'Percentage of households with two '
             'cars or vans in the buffer area','Number of cars or vans: 3 or more cars or vans in household',
             'Percentage of households with three or more cars of vans in the buffer area')

# DWELLINGS
census_stats(Dwellings, ProjLSOA, resultsfile, 'Dwelling types in the project area', 'Accommodation type: Total: '
            'All households', 'Accommodation type: Detached', 'Percentage of detached houses in the project area',
             'Accommodation type: Semi-detached', 'Percentage of semi-detached houses in the project area',
             'Accommodation type: Terraced', 'Percentage of terraced houses in the project area', 'Accommodation type: '
            'In a purpose-built block of flats or tenement', 'Percentage of dwellings in a purpose-built block of flats'
            ' or tenement in the project area', 'Accommodation type: Part of a converted or shared house, including '
            'bedsits', 'Percentage of dwellings in part of a converted or shared house, including bedsits, in the '
                       'project area', 'Accommodation type: Part of another converted building, for example, former '
                        'school, church or warehouse', 'Percentage of dwellings in part of another converted building '
                        'in the project area', 'Accommodation type: In a commercial building, for example, in an office'
                        ' building, hotel or over a shop', 'Percentage of dwellings in a commercial building in the '
                        'project area (e.g. in an office building, hotel or over a shop', 'Accommodation type: A '
                        'caravan or other mobile or temporary structure', 'Percentage of dwellings in a caravan or '
                        'other mobile or temporary structure in the project area')

census_stats(Dwellings, BuffLSOA, resultsfile, 'Dwelling types in the 4 mile buffer area', 'Accommodation type: Total:'
            ' All households', 'Accommodation type: Detached', 'Percentage of detached houses in the buffer area',
             'Accommodation type: Semi-detached', 'Percentage of semi-detached houses in the buffer area',
             'Accommodation type: Terraced', 'Percentage of terraced houses in the buffer area', 'Accommodation type: '
            'In a purpose-built block of flats or tenement', 'Percentage of dwellings in a purpose-built block of flats'
            ' or tenement in the buffer area', 'Accommodation type: Part of a converted or shared house, including '
            'bedsits', 'Percentage of dwellings in part of a converted or shared house, including bedsits, in the '
                       'buffer area', 'Accommodation type: Part of another converted building, for example, former '
                        'school, church or warehouse', 'Percentage of dwellings in part of another converted building '
                        'in the buffer area', 'Accommodation type: In a commercial building, for example, in an office'
                        ' building, hotel or over a shop', 'Percentage of dwellings in a commercial building in the '
                        'buffer area (e.g. in an office building, hotel or over a shop', 'Accommodation type: A '
                        'caravan or other mobile or temporary structure', 'Percentage of dwellings in a caravan or '
                        'other mobile or temporary structure in the buffer area')

census_stats(Dwellings, Buff2LSOA, resultsfile, 'Dwelling types in the 8 mile buffer area', 'Accommodation type: Total:'
            ' All households', 'Accommodation type: Detached', 'Percentage of detached houses in the buffer area',
             'Accommodation type: Semi-detached', 'Percentage of semi-detached houses in the buffer area',
             'Accommodation type: Terraced', 'Percentage of terraced houses in the buffer area', 'Accommodation type: '
            'In a purpose-built block of flats or tenement', 'Percentage of dwellings in a purpose-built block of flats'
            ' or tenement in the buffer area', 'Accommodation type: Part of a converted or shared house, including '
            'bedsits', 'Percentage of dwellings in part of a converted or shared house, including bedsits, in the '
                       'buffer area', 'Accommodation type: Part of another converted building, for example, former '
                        'school, church or warehouse', 'Percentage of dwellings in part of another converted building '
                        'in the buffer area', 'Accommodation type: In a commercial building, for example, in an office'
                        ' building, hotel or over a shop', 'Percentage of dwellings in a commercial building in the '
                        'buffer area (e.g. in an office building, hotel or over a shop', 'Accommodation type: A '
                        'caravan or other mobile or temporary structure', 'Percentage of dwellings in a caravan or '
                        'other mobile or temporary structure in the buffer area')

# DEPRIVATION DIMENSIONS
census_stats(DeprivationDimensions, ProjLSOA, resultsfile, 'Household deprivation dimensions in the project area. '
                        '(Census 2021 estimates that classify households in England '
                        'and Wales by four dimensions of deprivation: Employment, '
                        'education, health and disability, and household '
                        'overcrowding. The estimates are as at Census Day, 21 March '
                        '2021.)', 'Household deprivation: Total: All households; '
    'measures: Value', 'Household deprivation: Household is not deprived in any dimension; measures: Value', 'Percentage'
     ' of households in the project area which are not deprived in any dimension', 'Household deprivation: Household is'
     ' deprived in one dimension; measures: Value', 'Percentage of households in the project area which are deprived '
        'in one dimension', 'Household deprivation: Household is deprived in two dimensions; measures: Value',
        'Percentage of households in the project area which are deprived in two dimensions', 'Household deprivation: '
         'Household is deprived in three dimensions; measures: Value', 'Percentage of households in the project area '
         'which are deprived in three dimensions', 'Household deprivation: Household is deprived in four dimensions; '
        'measures: Value', 'Percentage of households in the project area which are deprived in four dimensions')

census_stats(DeprivationDimensions, BuffLSOA, resultsfile, 'Household deprivation dimensions in the 4 mile buffer'
                                                           ' area. (Census 2021 estimates that classify households in England '
                                                           'and Wales by four dimensions of deprivation: Employment, '
                                                           'education, health and disability, and household '
                                                           'overcrowding. The estimates are as at Census Day, 21 March '
                                                           '2021.)', 'Household deprivation: Total: All households; '
    'measures: Value', 'Household deprivation: Household is not deprived in any dimension; measures: Value', 'Percentage'
     ' of households in the buffer area which are not deprived in any dimension', 'Household deprivation: Household is'
     ' deprived in one dimension; measures: Value', 'Percentage of households in the buffer area which are deprived '
        'in one dimension', 'Household deprivation: Household is deprived in two dimensions; measures: Value',
        'Percentage of households in the buffer area which are deprived in two dimensions', 'Household deprivation: '
         'Household is deprived in three dimensions; measures: Value', 'Percentage of households in the buffer area '
         'which are deprived in three dimensions', 'Household deprivation: Household is deprived in four dimensions; '
        'measures: Value', 'Percentage of households in the buffer area which are deprived in four dimensions')

census_stats(DeprivationDimensions, Buff2LSOA, resultsfile, 'Household deprivation dimensions in the 8 mile buffer'
                                                           ' area. (Census 2021 estimates that classify households in England '
                                                           'and Wales by four dimensions of deprivation: Employment, '
                                                           'education, health and disability, and household '
                                                           'overcrowding. The estimates are as at Census Day, 21 March '
                                                           '2021.)', 'Household deprivation: Total: All households; '
    'measures: Value', 'Household deprivation: Household is not deprived in any dimension; measures: Value', 'Percentage'
     ' of households in the buffer area which are not deprived in any dimension', 'Household deprivation: Household is'
     ' deprived in one dimension; measures: Value', 'Percentage of households in the buffer area which are deprived '
        'in one dimension', 'Household deprivation: Household is deprived in two dimensions; measures: Value',
        'Percentage of households in the buffer area which are deprived in two dimensions', 'Household deprivation: '
         'Household is deprived in three dimensions; measures: Value', 'Percentage of households in the buffer area '
         'which are deprived in three dimensions', 'Household deprivation: Household is deprived in four dimensions; '
        'measures: Value', 'Percentage of households in the buffer area which are deprived in four dimensions')

# HIGHEST LEVEL OF EDUCATION
census_stats(HighestEd, ProjLSOA, resultsfile, 'Highest levels of education in the project area - residents aged 16 and'
    'over', 'Highest level of qualification: Total: All usual residents aged 16 years and over', 'Highest level of '
    'qualification: No qualifications', 'Percentage of residents in the project area with no qualifications', 'Highest '
    'level of qualification: Level 1 and entry level qualifications', 'Percentage of residents in the project area with'
    'Level 1 and entry level qualifications', 'Highest level of qualification: Level 2 qualifications', 'Percentage of '
    'residents in the project area with Level 2 qualifications', 'Highest level of qualification: Apprenticeship',
    'Percentage of residents in the project area that have completed an apprenticeship', 'Highest level of '
    'qualification: Level 3 qualifications', 'Percentage of residents in the project area with Level 3 qualifications',
    'Highest level of qualification: Level 4 qualifications and above', 'Percentage of residents in the project area '
    'with Level 4 qualifications and above', 'Highest level of qualification: Other qualifications', 'Percentage '
    'of residents in the project area with other qualifications')

census_stats(HighestEd, BuffLSOA, resultsfile, 'Highest levels of education in the 4 mile buffer area - residents '
    'aged 16 and over', 'Highest level of qualification: Total: All usual residents aged 16 years and over',
     'Highest level of qualification: No qualifications', 'Percentage of residents in the buffer area with no '
     'qualifications', 'Highest level of qualification: Level 1 and entry level qualifications', 'Percentage of '
     'residents in the buffer area with Level 1 and entry level qualifications', 'Highest level of qualification: '
     'Level 2 qualifications', 'Percentage of residents in the buffer area with Level 2 qualifications', 'Highest '
     'level of qualification: Apprenticeship', 'Percentage of residents in the buffer area that have completed an '
     'apprenticeship', 'Highest level of qualification: Level 3 qualifications', 'Percentage of residents in the '
     'buffer area with Level 3 qualifications', 'Highest level of qualification: Level 4 qualifications and above',
    'Percentage of residents in the buffer area with Level 4 qualifications and above', 'Highest level of '
     'qualification: Other qualifications', 'Percentage of residents in the buffer area with other qualifications')

census_stats(HighestEd, Buff2LSOA, resultsfile, 'Highest levels of education in the 8 mile buffer area - residents '
    'aged 16 and over', 'Highest level of qualification: Total: All usual residents aged 16 years and over',
     'Highest level of qualification: No qualifications', 'Percentage of residents in the buffer area with no '
     'qualifications', 'Highest level of qualification: Level 1 and entry level qualifications', 'Percentage of '
     'residents in the buffer area with Level 1 and entry level qualifications', 'Highest level of qualification: '
     'Level 2 qualifications', 'Percentage of residents in the buffer area with Level 2 qualifications', 'Highest '
     'level of qualification: Apprenticeship', 'Percentage of residents in the buffer area that have completed an '
     'apprenticeship', 'Highest level of qualification: Level 3 qualifications', 'Percentage of residents in the '
     'buffer area with Level 3 qualifications', 'Highest level of qualification: Level 4 qualifications and above',
    'Percentage of residents in the buffer area with Level 4 qualifications and above', 'Highest level of '
     'qualification: Other qualifications', 'Percentage of residents in the buffer area with other qualifications')

# ETHNICITY
census_stats(Ethnicity, ProjLSOA, resultsfile, 'Ethnicity of residents in the project area', 'Ethnic group: Total: '
      'All usual residents', 'Ethnic group: Asian, Asian British or Asian Welsh', 'Percentage of residents in the '
      'project area who are Asian, Asian British or Asian Welsh', 'Ethnic group: Black, Black British, Black Welsh, '
      'Caribbean or African', 'Percentage of residents in the project area who are Black, Black British, Black '
      'Welsh, Caribbean or African', 'Ethnic group: Mixed or Multiple ethnic groups', 'Percentage of residents in '
      'the project area from mixed or multiple ethnic groups', 'Ethnic group: White', 'Percentage of residents in '
      'the project area who are White', 'Ethnic group: White: Gypsy or Irish Traveller', 'Percentage of residents '
      'in the project area who are White Gypsy or Irish Traveller', 'Ethnic group: White: Roma', 'Percentage '
      'of residents in the project area who are White Roma', 'Ethnic group: Other ethnic group', 'Percentage of '
      'residents in the project area from other ethnic groups')

census_stats(Ethnicity, BuffLSOA, resultsfile, 'Ethnicity of residents in the 4 mile buffer area', 'Ethnic group: '
      'Total: All usual residents', 'Ethnic group: Asian, Asian British or Asian Welsh', 'Percentage of residents in '
      'the buffer area who are Asian, Asian British or Asian Welsh', 'Ethnic group: Black, Black British, Black Welsh,'
      ' Caribbean or African', 'Percentage of residents in the buffer area who are Black, Black British, Black '
      'Welsh, Caribbean or African', 'Ethnic group: Mixed or Multiple ethnic groups', 'Percentage of residents in '
      'the buffer area from mixed or multiple ethnic groups', 'Ethnic group: White', 'Percentage of residents in '
      'the buffer area who are White', 'Ethnic group: White: Gypsy or Irish Traveller', 'Percentage of residents '
      'in the buffer area who are White Gypsy or Irish Traveller', 'Ethnic group: White: Roma', 'Percentage '
      'of residents in the buffer area who are White Roma', 'Ethnic group: Other ethnic group', 'Percentage of '
      'residents in the buffer area from other ethnic groups')

census_stats(Ethnicity, Buff2LSOA, resultsfile, 'Ethnicity of residents in the 8 mile buffer area', 'Ethnic group: '
      'Total: All usual residents', 'Ethnic group: Asian, Asian British or Asian Welsh', 'Percentage of residents in '
      'the buffer area who are Asian, Asian British or Asian Welsh', 'Ethnic group: Black, Black British, Black Welsh,'
      ' Caribbean or African', 'Percentage of residents in the buffer area who are Black, Black British, Black '
      'Welsh, Caribbean or African', 'Ethnic group: Mixed or Multiple ethnic groups', 'Percentage of residents in '
      'the buffer area from mixed or multiple ethnic groups', 'Ethnic group: White', 'Percentage of residents in '
      'the buffer area who are White', 'Ethnic group: White: Gypsy or Irish Traveller', 'Percentage of residents '
      'in the buffer area who are White Gypsy or Irish Traveller', 'Ethnic group: White: Roma', 'Percentage '
      'of residents in the buffer area who are White Roma', 'Ethnic group: Other ethnic group', 'Percentage of '
      'residents in the buffer area from other ethnic groups')

# HEALTH
census_stats(Health, ProjLSOA, resultsfile, 'General health of residents in the project area',
       'General health: Total: All usual residents', 'General health: Very good health', 'Percentage of residents '
       'in the project area with very good health', 'General health: Good health', 'Percentage of residents in the '
       'project area with good health', 'General health: Fair health', 'Percentage of residents in the project area '
       'with fair health', 'General health: Bad health', 'Percentage of residents in the project area with bad health',
        'General health: Very bad health', 'Percentage of residents in the project area with very bad health')

census_stats(Health, BuffLSOA, resultsfile, 'General health of residents in the 4 mile buffer area',
       'General health: Total: All usual residents', 'General health: Very good health', 'Percentage of residents '
       'in the buffer area with very good health', 'General health: Good health', 'Percentage of residents in the '
       'buffer area with good health', 'General health: Fair health', 'Percentage of residents in the buffer area '
       'with fair health', 'General health: Bad health', 'Percentage of residents in the buffer area with bad health',
       'General health: Very bad health', 'Percentage of residents in the buffer area with very bad health')

census_stats(Health, Buff2LSOA, resultsfile, 'General health of residents in the 8 mile buffer area',
       'General health: Total: All usual residents', 'General health: Very good health', 'Percentage of residents '
       'in the buffer area with very good health', 'General health: Good health', 'Percentage of residents in the '
       'buffer area with good health', 'General health: Fair health', 'Percentage of residents in the buffer area '
       'with fair health', 'General health: Bad health', 'Percentage of residents in the buffer area with bad health',
       'General health: Very bad health', 'Percentage of residents in the buffer area with very bad health')

# DISABILITY
census_stats(Disability, ProjLSOA, resultsfile, 'Disability in the project area',
             'Disability: Total: All usual residents', 'Disability: Disabled under the Equality Act', 'Percentage '
             'of residents in the project area who are disabled under the Equality Act', 'Disability: Disabled '
             'under the Equality Act: Day-to-day activities limited a lot', 'Percentage of residents in the project '
             'area who are disabled and whose day-to-day activities are limited a lot', 'Disability: Disabled '
             'under the Equality Act: Day-to-day activities limited a little', 'Percentage of residents in the project '
             'area who are disabled and whose day-to-day activities are limited a little', 'Disability: Not disabled '
             'under the Equality Act', 'Percentage of residents in the project area who are not disabled under the '
             'Equality Act', 'Disability: Not disabled under the Equality Act: Has long term physical or mental '
             'health condition but day-to-day activities are not limited', 'Percentage of residents in the project '
             'area who are not disabled but have a long term physical or mental health condition', 'Disability: Not '
             'disabled under the Equality Act: No long term physical or mental health conditions', 'Percentage of '
             'residents in the project area who have no long term physical or mental health conditions')

census_stats(Disability, BuffLSOA, resultsfile, 'Disability in the 4 mile buffer area',
             'Disability: Total: All usual residents', 'Disability: Disabled under the Equality Act', 'Percentage '
             'of residents in the buffer area who are disabled under the Equality Act', 'Disability: Disabled '
             'under the Equality Act: Day-to-day activities limited a lot', 'Percentage of residents in the buffer '
             'area who are disabled and whose day-to-day activities are limited a lot', 'Disability: Disabled '
             'under the Equality Act: Day-to-day activities limited a little', 'Percentage of residents in the buffer '
             'area who are disabled and whose day-to-day activities are limited a little', 'Disability: Not disabled '
             'under the Equality Act', 'Percentage of residents in the buffer area who are not disabled under the '
             'Equality Act', 'Disability: Not disabled under the Equality Act: Has long term physical or mental '
             'health condition but day-to-day activities are not limited', 'Percentage of residents in the buffer '
             'area who are not disabled but have a long term physical or mental health condition', 'Disability: Not '
             'disabled under the Equality Act: No long term physical or mental health conditions', 'Percentage of '
             'residents in the buffer area who have no long term physical or mental health conditions')

census_stats(Disability, Buff2LSOA, resultsfile, 'Disability in the 8 mile buffer area',
             'Disability: Total: All usual residents', 'Disability: Disabled under the Equality Act', 'Percentage '
             'of residents in the buffer area who are disabled under the Equality Act', 'Disability: Disabled '
             'under the Equality Act: Day-to-day activities limited a lot', 'Percentage of residents in the buffer '
             'area who are disabled and whose day-to-day activities are limited a lot', 'Disability: Disabled '
             'under the Equality Act: Day-to-day activities limited a little', 'Percentage of residents in the buffer '
             'area who are disabled and whose day-to-day activities are limited a little', 'Disability: Not disabled '
             'under the Equality Act', 'Percentage of residents in the buffer area who are not disabled under the '
             'Equality Act', 'Disability: Not disabled under the Equality Act: Has long term physical or mental '
             'health condition but day-to-day activities are not limited', 'Percentage of residents in the buffer '
             'area who are not disabled but have a long term physical or mental health condition', 'Disability: Not '
             'disabled under the Equality Act: No long term physical or mental health conditions', 'Percentage of '
             'residents in the buffer area who have no long term physical or mental health conditions')

# UNPAID CARE
census_stats(UnpaidCare, ProjLSOA, resultsfile, 'Unpaid care provision in the project area (residents = all usual '
                                                'residents aged 5 and over)',
             'Provision of unpaid care: Total: All usual residents aged 5 and over', 'Provision of unpaid care: '
             'Provides no unpaid care', 'Percentage of residents in the project area who do not provide unpaid care',
             'Provision of unpaid care: Provides 19 hours or less unpaid care a week', 'Percentage of residents '
             'in the project area who provide 19 hours or less unpaid care a week', 'Provision of unpaid care: '
             'Provides 20 to 49 hours unpaid care a week', 'Percentage of residents in the project area who provide '
             '20 to 49 hours unpaid care a week', 'Provision of unpaid care: Provides 50 or more hours unpaid care '
             'a week', 'Percentage of residents in the project area who provide 50 or more hours unpaid care a week')

census_stats(UnpaidCare, BuffLSOA, resultsfile, 'Unpaid care provision in the 4 mile buffer area (residents = all '
                                                'usual residents aged 5 and over)',
             'Provision of unpaid care: Total: All usual residents aged 5 and over', 'Provision of unpaid care: '
             'Provides no unpaid care', 'Percentage of residents in the buffer area who do not provide unpaid care',
             'Provision of unpaid care: Provides 19 hours or less unpaid care a week', 'Percentage of residents '
             'in the buffer area who provide 19 hours or less unpaid care a week', 'Provision of unpaid care: '
             'Provides 20 to 49 hours unpaid care a week', 'Percentage of residents in the buffer area who provide '
             '20 to 49 hours unpaid care a week', 'Provision of unpaid care: Provides 50 or more hours unpaid care '
             'a week', 'Percentage of residents in the buffer area who provide 50 or more hours unpaid care a week')

census_stats(UnpaidCare, Buff2LSOA, resultsfile, 'Unpaid care provision in the 8 mile buffer area (residents = all '
                                                'usual residents aged 5 and over)',
             'Provision of unpaid care: Total: All usual residents aged 5 and over', 'Provision of unpaid care: '
             'Provides no unpaid care', 'Percentage of residents in the buffer area who do not provide unpaid care',
             'Provision of unpaid care: Provides 19 hours or less unpaid care a week', 'Percentage of residents '
             'in the buffer area who provide 19 hours or less unpaid care a week', 'Provision of unpaid care: '
             'Provides 20 to 49 hours unpaid care a week', 'Percentage of residents in the buffer area who provide '
             '20 to 49 hours unpaid care a week', 'Provision of unpaid care: Provides 50 or more hours unpaid care '
             'a week', 'Percentage of residents in the buffer area who provide 50 or more hours unpaid care a week')

# HOURS WORKED
census_stats(HoursWorked, ProjLSOA, resultsfile, 'Hours worked in the project area '
             '(residents 16+ and in employment 1 week before the census)',
             'Hours worked: Total: All usual residents aged 16 years and over in employment the week before the '
             'census', 'Hours worked: Part-time: 15 hours or less worked', 'Percentage of employed residents in the '
             'project area working 15 hours or less', 'Hours worked: Part-time: 16 to 30 hours worked', 'Percentage '
             'of employed residents in the project area working 16-30 hours', 'Hours worked: Full-time: 31 to 48 '
             'hours worked', 'Percentage of employed residents in the project area working 31-48 hours', 'Hours '
             'worked: Full-time: 49 or more hours worked', 'Percentage of employed residents in the project area '
             'working 49+ hours')

census_stats(HoursWorked, BuffLSOA, resultsfile, 'Hours worked in the 4 mile buffer area '
             '(residents 16+ and in employment 1 week before the census)',
             'Hours worked: Total: All usual residents aged 16 years and over in employment the week before the '
             'census', 'Hours worked: Part-time: 15 hours or less worked', 'Percentage of employed residents in the '
             'buffer area working 15 hours or less', 'Hours worked: Part-time: 16 to 30 hours worked', 'Percentage '
             'of employed residents in the buffer area working 16-30 hours', 'Hours worked: Full-time: 31 to 48 '
             'hours worked', 'Percentage of employed residents in the buffer area working 31-48 hours', 'Hours '
             'worked: Full-time: 49 or more hours worked', 'Percentage of employed residents in the buffer area '
             'working 49+ hours')

census_stats(HoursWorked, Buff2LSOA, resultsfile, 'Hours worked in the 8 mile buffer area '
             '(residents 16+ and in employment 1 week before the census)',
             'Hours worked: Total: All usual residents aged 16 years and over in employment the week before the '
             'census', 'Hours worked: Part-time: 15 hours or less worked', 'Percentage of employed residents in the '
             'buffer area working 15 hours or less', 'Hours worked: Part-time: 16 to 30 hours worked', 'Percentage '
             'of employed residents in the buffer area working 16-30 hours', 'Hours worked: Full-time: 31 to 48 '
             'hours worked', 'Percentage of employed residents in the buffer area working 31-48 hours', 'Hours '
             'worked: Full-time: 49 or more hours worked', 'Percentage of employed residents in the buffer area '
             'working 49+ hours')

# HOUSEHOLD COMPOSITION
census_stats(HouseholdComposition, ProjLSOA, resultsfile, 'Household composition in the project area',
             'Household composition: Total; measures: Value', 'Household composition: One person household; '
             'measures: Value', 'Percentage of households in the project area which are one person', 'Household '
             'composition: One person household: Aged 66 years and over; measures: Value', 'Percentage of households '
             'in the project area of one person aged 66 and over', 'Household composition: One person household: '
             'Other; measures: Value', 'Percentage of households in the project area of one person 65 and under',
             'Household composition: Single family household; measures: Value', 'Percentage of households in the '
             'project area which are single-family', 'Household composition: Single family household: All aged '
             '66 years and over; measures: Value', 'Percentage of households in the project area which are '
             'single-family all aged 66 and over', 'Household composition: Single family household: Married or '
             'civil partnership couple; measures: Value', 'Percentage of households in the project area which are '
             'single-family including a married or civil-partnership couple', 'Household composition: Single family '
             'household: Married or civil partnership couple: No children; measures: Value', 'Percentage of households '
             'in the project area which are single-family - married or civil partnership couple with no children',
             'Household composition: Single family household: Married or civil partnership couple: Dependent children; '
             'measures: Value', 'Percentage of households in the project area which are single-family - married or '
             'civil partnership couple with dependent children', 'Household composition: Single family household: '
             'Married or civil partnership couple: All children non-dependent; measures: Value', 'Percentage of '
             'households in the project area which are single-family - married or civil partnership couple with '
             'all children non-dependent', 'Household composition: Single family household: Cohabiting couple family; '
             'measures: Value', 'Percentage of households in the project area which are single-family including '
             'a cohabiting couple', 'Household composition: Single family household: Cohabiting couple family: No '
             'children; measures: Value', 'Percentage of households in the project area which are single-family - '
             'cohabiting couple with no children', 'Household composition: Single family household: Cohabiting couple '
             'family: With dependent children; measures: Value', 'Percentage of households in the project area which '
             'are single-family - cohabiting couple with dependent children', 'Household composition: Single family '
             'household: Cohabiting couple family: All children non-dependent; measures: Value', 'Percentage of '
             'households in the project area which are single-family - cohabiting couple with all children '
             'non-dependent', 'Household composition: Single family household: Lone parent family; measures: Value',
             'Percentage of households in the project area which are single-family with a lone parent', 'Household '
             'composition: Single family household: Lone parent family: With dependent children; measures: Value',
             'Percentage of households in the project area which are single-family - lone parent with dependent '
             'children', 'Household composition: Single family household: Lone parent family: All children '
             'non-dependent; measures: Value', 'Percentage of households in the project area with a single lone-parent'
             ' family where all children are non-dependent', 'Household composition: Single family household: Other '
             'single family household; measures: Value', 'Percentage of households in the project area which are '
             'other single-family households', 'Household composition: Other household types: With dependent children; '
             'measures: Value', 'Percentage of households in the project area which are other household types with '
             'dependent children', 'Household composition: Other household types: Other, including all full-time '
             'students and all aged 66 years and over; measures: Value', 'Percentage of households in the project area '
             'which are other household types including all full-time students and all aged 66+')

census_stats(HouseholdComposition, BuffLSOA, resultsfile, 'Household composition in the 4 mile buffer area',
             'Household composition: Total; measures: Value', 'Household composition: One person household; '
             'measures: Value', 'Percentage of households in the buffer area which are one person', 'Household '
             'composition: One person household: Aged 66 years and over; measures: Value', 'Percentage of households '
             'in the buffer area of one person aged 66 and over', 'Household composition: One person household: '
             'Other; measures: Value', 'Percentage of households in the buffer area of one person 65 and under',
             'Household composition: Single family household; measures: Value', 'Percentage of households in the '
             'buffer area which are single-family', 'Household composition: Single family household: All aged '
             '66 years and over; measures: Value', 'Percentage of households in the buffer area which are '
             'single-family all aged 66 and over', 'Household composition: Single family household: Married or '
             'civil partnership couple; measures: Value', 'Percentage of households in the buffer area which are '
             'single-family including a married or civil-partnership couple', 'Household composition: Single family '
             'household: Married or civil partnership couple: No children; measures: Value', 'Percentage of households '
             'in the buffer area which are single-family - married or civil partnership couple with no children',
             'Household composition: Single family household: Married or civil partnership couple: Dependent children; '
             'measures: Value', 'Percentage of households in the buffer area which are single-family - married or '
             'civil partnership couple with dependent children', 'Household composition: Single family household: '
             'Married or civil partnership couple: All children non-dependent; measures: Value', 'Percentage of '
             'households in the buffer area which are single-family - married or civil partnership couple with '
             'all children non-dependent', 'Household composition: Single family household: Cohabiting couple family; '
             'measures: Value', 'Percentage of households in the buffer area which are single-family including '
             'a cohabiting couple', 'Household composition: Single family household: Cohabiting couple family: No '
             'children; measures: Value', 'Percentage of households in the buffer area which are single-family - '
             'cohabiting couple with no children', 'Household composition: Single family household: Cohabiting couple '
             'family: With dependent children; measures: Value', 'Percentage of households in the buffer area which '
             'are single-family - cohabiting couple with dependent children', 'Household composition: Single family '
             'household: Cohabiting couple family: All children non-dependent; measures: Value', 'Percentage of '
             'households in the buffer area which are single-family - cohabiting couple with all children '
             'non-dependent', 'Household composition: Single family household: Lone parent family; measures: Value',
             'Percentage of households in the buffer area which are single-family with a lone parent', 'Household '
             'composition: Single family household: Lone parent family: With dependent children; measures: Value',
             'Percentage of households in the buffer area which are single-family - lone parent with dependent '
             'children', 'Household composition: Single family household: Lone parent family: All children '
             'non-dependent; measures: Value', 'Percentage of households in the buffer area with a single lone-parent'
             ' family where all children are non-dependent', 'Household composition: Single family household: Other '
             'single family household; measures: Value', 'Percentage of households in the buffer area which are '
             'other single-family households', 'Household composition: Other household types: With dependent children; '
             'measures: Value', 'Percentage of households in the buffer area which are other household types with '
             'dependent children', 'Household composition: Other household types: Other, including all full-time '
             'students and all aged 66 years and over; measures: Value', 'Percentage of households in the buffer area '
             'which are other household types including all full-time students and all aged 66+')

census_stats(HouseholdComposition, Buff2LSOA, resultsfile, 'Household composition in the 8 mile buffer area',
             'Household composition: Total; measures: Value', 'Household composition: One person household; '
             'measures: Value', 'Percentage of households in the buffer area which are one person', 'Household '
             'composition: One person household: Aged 66 years and over; measures: Value', 'Percentage of households '
             'in the buffer area of one person aged 66 and over', 'Household composition: One person household: '
             'Other; measures: Value', 'Percentage of households in the buffer area of one person 65 and under',
             'Household composition: Single family household; measures: Value', 'Percentage of households in the '
             'buffer area which are single-family', 'Household composition: Single family household: All aged '
             '66 years and over; measures: Value', 'Percentage of households in the buffer area which are '
             'single-family all aged 66 and over', 'Household composition: Single family household: Married or '
             'civil partnership couple; measures: Value', 'Percentage of households in the buffer area which are '
             'single-family including a married or civil-partnership couple', 'Household composition: Single family '
             'household: Married or civil partnership couple: No children; measures: Value', 'Percentage of households '
             'in the buffer area which are single-family - married or civil partnership couple with no children',
             'Household composition: Single family household: Married or civil partnership couple: Dependent children; '
             'measures: Value', 'Percentage of households in the buffer area which are single-family - married or '
             'civil partnership couple with dependent children', 'Household composition: Single family household: '
             'Married or civil partnership couple: All children non-dependent; measures: Value', 'Percentage of '
             'households in the buffer area which are single-family - married or civil partnership couple with '
             'all children non-dependent', 'Household composition: Single family household: Cohabiting couple family; '
             'measures: Value', 'Percentage of households in the buffer area which are single-family including '
             'a cohabiting couple', 'Household composition: Single family household: Cohabiting couple family: No '
             'children; measures: Value', 'Percentage of households in the buffer area which are single-family - '
             'cohabiting couple with no children', 'Household composition: Single family household: Cohabiting couple '
             'family: With dependent children; measures: Value', 'Percentage of households in the buffer area which '
             'are single-family - cohabiting couple with dependent children', 'Household composition: Single family '
             'household: Cohabiting couple family: All children non-dependent; measures: Value', 'Percentage of '
             'households in the buffer area which are single-family - cohabiting couple with all children '
             'non-dependent', 'Household composition: Single family household: Lone parent family; measures: Value',
             'Percentage of households in the buffer area which are single-family with a lone parent', 'Household '
             'composition: Single family household: Lone parent family: With dependent children; measures: Value',
             'Percentage of households in the buffer area which are single-family - lone parent with dependent '
             'children', 'Household composition: Single family household: Lone parent family: All children '
             'non-dependent; measures: Value', 'Percentage of households in the buffer area with a single lone-parent'
             ' family where all children are non-dependent', 'Household composition: Single family household: Other '
             'single family household; measures: Value', 'Percentage of households in the buffer area which are '
             'other single-family households', 'Household composition: Other household types: With dependent children; '
             'measures: Value', 'Percentage of households in the buffer area which are other household types with '
             'dependent children', 'Household composition: Other household types: Other, including all full-time '
             'students and all aged 66 years and over; measures: Value', 'Percentage of households in the buffer area '
             'which are other household types including all full-time students and all aged 66+')

# OCCUPATION
census_stats(Occupation, ProjLSOA, resultsfile, 'Occupation of residents in the project area '
                                                '(16+ and employed the week before the census)',
             'Occupation (current): Total: All usual residents aged 16 years and over in employment the week before '
             'the census', 'Occupation (current): 1. Managers, directors and senior officials', 'Managers, directors '
             'and senior officials', 'Occupation (current): 2. Professional occupations', 'Professional occupations',
             'Occupation (current): 3. Associate professional and technical occupations', 'Associate professional and '
             'technical occupations', 'Occupation (current): 4. Administrative and secretarial occupations',
             'Administrative and secretarial occupations', 'Occupation (current): 5. Skilled trades occupations',
             'Skilled trades occupations', 'Occupation (current): 6. Caring, leisure and other service occupations',
             'Caring, leisure and other service occupations', 'Occupation (current): 7. Sales and customer service '
             'occupations', 'Sales and customer service occupations', 'Occupation (current): 8. Process, plant and '
             'machine operatives', 'Process, plant and machine operatives', 'Occupation (current): 9. Elementary '
             'occupations', 'Elementary occupations')

census_stats(Occupation, BuffLSOA, resultsfile, 'Occupation of residents in the 4 mile buffer area '
                                                '(16+ and employed the week before the census)',
             'Occupation (current): Total: All usual residents aged 16 years and over in employment the week before '
             'the census', 'Occupation (current): 1. Managers, directors and senior officials', 'Managers, directors '
             'and senior officials', 'Occupation (current): 2. Professional occupations', 'Professional occupations',
             'Occupation (current): 3. Associate professional and technical occupations', 'Associate professional and '
             'technical occupations', 'Occupation (current): 4. Administrative and secretarial occupations',
             'Administrative and secretarial occupations', 'Occupation (current): 5. Skilled trades occupations',
             'Skilled trades occupations', 'Occupation (current): 6. Caring, leisure and other service occupations',
             'Caring, leisure and other service occupations', 'Occupation (current): 7. Sales and customer service '
             'occupations', 'Sales and customer service occupations', 'Occupation (current): 8. Process, plant and '
             'machine operatives', 'Process, plant and machine operatives', 'Occupation (current): 9. Elementary '
             'occupations', 'Elementary occupations')

census_stats(Occupation, Buff2LSOA, resultsfile, 'Occupation of residents in the 8 mile buffer area '
                                                '(16+ and employed the week before the census)',
             'Occupation (current): Total: All usual residents aged 16 years and over in employment the week before '
             'the census', 'Occupation (current): 1. Managers, directors and senior officials', 'Managers, directors '
             'and senior officials', 'Occupation (current): 2. Professional occupations', 'Professional occupations',
             'Occupation (current): 3. Associate professional and technical occupations', 'Associate professional and '
             'technical occupations', 'Occupation (current): 4. Administrative and secretarial occupations',
             'Administrative and secretarial occupations', 'Occupation (current): 5. Skilled trades occupations',
             'Skilled trades occupations', 'Occupation (current): 6. Caring, leisure and other service occupations',
             'Caring, leisure and other service occupations', 'Occupation (current): 7. Sales and customer service '
             'occupations', 'Sales and customer service occupations', 'Occupation (current): 8. Process, plant and '
             'machine operatives', 'Process, plant and machine operatives', 'Occupation (current): 9. Elementary '
             'occupations', 'Elementary occupations')

# LEGAL PARTNERSHIP
census_stats(LegalPartnership, ProjLSOA, resultsfile, 'Legal partnership of residents in the project area',
             'Marital and civil partnership status: Total; measures: Value', 'Marital and civil partnership status: '
             'Never married and never registered a civil partnership; measures: Value', 'Never married and never '
             'registered a civil partnership', 'Marital and civil partnership status: Married or in a registered '
             'civil partnership: Married; measures: Value', 'Married', 'Marital and civil partnership status: Married '
             'or in a registered civil partnership: Married: Same sex; measures: Value', 'Married (same sex marriage)',
             'Marital and civil partnership status: Married or in a registered civil partnership: In a registered '
             'civil partnership: Same sex; measures: Value', 'In a same sex registered civil partnership', 'Marital '
             'and civil partnership status: Separated, but still legally married or still legally in a civil '
             'partnership; measures: Value', 'Separated', 'Marital and civil partnership status: Divorced or civil '
             'partnership dissolved; measures: Value', 'Divorced or civil partnership dissolved', 'Marital and civil '
             'partnership status: Widowed or surviving civil partnership partner; measures: Value', 'Widowed or '
             'surviving civil partnership partner')

census_stats(LegalPartnership, BuffLSOA, resultsfile, 'Legal partnership of residents in the 4 mile buffer area',
             'Marital and civil partnership status: Total; measures: Value', 'Marital and civil partnership status: '
             'Never married and never registered a civil partnership; measures: Value', 'Never married and never '
             'registered a civil partnership', 'Marital and civil partnership status: Married or in a registered '
             'civil partnership: Married; measures: Value', 'Married', 'Marital and civil partnership status: Married '
             'or in a registered civil partnership: Married: Same sex; measures: Value', 'Married (same sex marriage)',
             'Marital and civil partnership status: Married or in a registered civil partnership: In a registered '
             'civil partnership: Same sex; measures: Value', 'In a same sex registered civil partnership', 'Marital '
             'and civil partnership status: Separated, but still legally married or still legally in a civil '
             'partnership; measures: Value', 'Separated', 'Marital and civil partnership status: Divorced or civil '
             'partnership dissolved; measures: Value', 'Divorced or civil partnership dissolved', 'Marital and civil '
             'partnership status: Widowed or surviving civil partnership partner; measures: Value', 'Widowed or '
             'surviving civil partnership partner')

census_stats(LegalPartnership, Buff2LSOA, resultsfile, 'Legal partnership of residents in the 8 mile buffer area',
             'Marital and civil partnership status: Total; measures: Value', 'Marital and civil partnership status: '
             'Never married and never registered a civil partnership; measures: Value', 'Never married and never '
             'registered a civil partnership', 'Marital and civil partnership status: Married or in a registered '
             'civil partnership: Married; measures: Value', 'Married', 'Marital and civil partnership status: Married '
             'or in a registered civil partnership: Married: Same sex; measures: Value', 'Married (same sex marriage)',
             'Marital and civil partnership status: Married or in a registered civil partnership: In a registered '
             'civil partnership: Same sex; measures: Value', 'In a same sex registered civil partnership', 'Marital '
             'and civil partnership status: Separated, but still legally married or still legally in a civil '
             'partnership; measures: Value', 'Separated', 'Marital and civil partnership status: Divorced or civil '
             'partnership dissolved; measures: Value', 'Divorced or civil partnership dissolved', 'Marital and civil '
             'partnership status: Widowed or surviving civil partnership partner; measures: Value', 'Widowed or '
             'surviving civil partnership partner')

# HOUSEHOLD LANGUAGE
census_stats(HouseholdLanguage, ProjLSOA, resultsfile, 'English spoken per household in the project area',
             'Household language (English and Welsh): Total: All households', 'Household language (English and Welsh): '
             'All adults in household have English in England, or English or Welsh in Wales as a main language',
             'All adults in household have English in England, or English or Welsh in Wales as a main language',
             'Household language (English and Welsh): At least one but not all adults in household have English in '
             'England, or English or Welsh in Wales as a main language', 'At least one but not all adults in household '
             'have English in England, or English or Welsh in Wales as a main language', 'Household language (English '
             'and Welsh): No adults in household, but at least one person aged 3 to 15 years, has English in England '
             'or English or Welsh in Wales as a main language', 'No adults in household, but at least one person aged '
             '3 to 15 years, has English in England or English or Welsh in Wales as a main language',
             'Household language (English and Welsh): No people in household have English in England, or English or '
             'Welsh in Wales as a main language', 'No people in household have English in England, or English or '
             'Welsh in Wales as a main language')

census_stats(HouseholdLanguage, BuffLSOA, resultsfile, 'English spoken per household in the 4 mile buffer area',
             'Household language (English and Welsh): Total: All households', 'Household language (English and Welsh): '
             'All adults in household have English in England, or English or Welsh in Wales as a main language',
             'All adults in household have English in England, or English or Welsh in Wales as a main language',
             'Household language (English and Welsh): At least one but not all adults in household have English in '
             'England, or English or Welsh in Wales as a main language', 'At least one but not all adults in household '
             'have English in England, or English or Welsh in Wales as a main language', 'Household language (English '
             'and Welsh): No adults in household, but at least one person aged 3 to 15 years, has English in England '
             'or English or Welsh in Wales as a main language', 'No adults in household, but at least one person aged '
             '3 to 15 years, has English in England or English or Welsh in Wales as a main language',
             'Household language (English and Welsh): No people in household have English in England, or English or '
             'Welsh in Wales as a main language', 'No people in household have English in England, or English or '
             'Welsh in Wales as a main language')

census_stats(HouseholdLanguage, Buff2LSOA, resultsfile, 'English spoken per household in the 8 mile buffer area',
             'Household language (English and Welsh): Total: All households', 'Household language (English and Welsh): '
             'All adults in household have English in England, or English or Welsh in Wales as a main language',
             'All adults in household have English in England, or English or Welsh in Wales as a main language',
             'Household language (English and Welsh): At least one but not all adults in household have English in '
             'England, or English or Welsh in Wales as a main language', 'At least one but not all adults in household '
             'have English in England, or English or Welsh in Wales as a main language', 'Household language (English '
             'and Welsh): No adults in household, but at least one person aged 3 to 15 years, has English in England '
             'or English or Welsh in Wales as a main language', 'No adults in household, but at least one person aged '
             '3 to 15 years, has English in England or English or Welsh in Wales as a main language',
             'Household language (English and Welsh): No people in household have English in England, or English or '
             'Welsh in Wales as a main language', 'No people in household have English in England, or English or '
             'Welsh in Wales as a main language')

# NS-SEC WORK TYPES
census_stats(NSEC, ProjLSOA, resultsfile, 'National Statistics Socio-economic Classification (NS-SEC) work types '
                                          'in the project area',
             'National Statistics Socio-economic Classification (NS-SEC): Total: All usual residents aged 16 years '
             'and over', 'National Statistics Socio-economic Classification (NS-SEC): L1, L2 and L3 Higher managerial, '
             'administrative and professional occupations', 'Higher managerial, administrative and professional '
             'occupations', 'National Statistics Socio-economic Classification (NS-SEC): L4, L5 and L6 Lower '
             'managerial, administrative and professional occupations', 'Lower managerial, administrative and '
             'professional occupations', 'National Statistics Socio-economic Classification (NS-SEC): L7 Intermediate '
             'occupations', 'Intermediate occupations', 'National Statistics Socio-economic Classification (NS-SEC): '
             'L8 and L9 Small employers and own account workers', 'Small employers and own account workers', 'National '
             'Statistics Socio-economic Classification (NS-SEC): L10 and L11 Lower supervisory and technical '
             'occupations', 'Lower supervisory and technical occupations', 'National Statistics Socio-economic '
             'Classification (NS-SEC): L12 Semi-routine occupations', 'Semi-routine occupations', 'National Statistics '
             'Socio-economic Classification (NS-SEC): L13 Routine occupations', 'Routine occupations', 'National '
             'Statistics Socio-economic Classification (NS-SEC): L14.1 and L14.2 Never worked and long-term unemployed',
             'Never worked and long-term unemployed', 'National Statistics Socio-economic Classification (NS-SEC): '
             'L15 Full-time students', 'Full-time students')

census_stats(NSEC, BuffLSOA, resultsfile, 'National Statistics Socio-economic Classification (NS-SEC) work types '
                                          'in the 4 mile buffer area',
             'National Statistics Socio-economic Classification (NS-SEC): Total: All usual residents aged 16 years '
             'and over', 'National Statistics Socio-economic Classification (NS-SEC): L1, L2 and L3 Higher managerial, '
             'administrative and professional occupations', 'Higher managerial, administrative and professional '
             'occupations', 'National Statistics Socio-economic Classification (NS-SEC): L4, L5 and L6 Lower '
             'managerial, administrative and professional occupations', 'Lower managerial, administrative and '
             'professional occupations', 'National Statistics Socio-economic Classification (NS-SEC): L7 Intermediate '
             'occupations', 'Intermediate occupations', 'National Statistics Socio-economic Classification (NS-SEC): '
             'L8 and L9 Small employers and own account workers', 'Small employers and own account workers', 'National '
             'Statistics Socio-economic Classification (NS-SEC): L10 and L11 Lower supervisory and technical '
             'occupations', 'Lower supervisory and technical occupations', 'National Statistics Socio-economic '
             'Classification (NS-SEC): L12 Semi-routine occupations', 'Semi-routine occupations', 'National Statistics '
             'Socio-economic Classification (NS-SEC): L13 Routine occupations', 'Routine occupations', 'National '
             'Statistics Socio-economic Classification (NS-SEC): L14.1 and L14.2 Never worked and long-term unemployed',
             'Never worked and long-term unemployed', 'National Statistics Socio-economic Classification (NS-SEC): '
             'L15 Full-time students', 'Full-time students')

census_stats(NSEC, Buff2LSOA, resultsfile, 'National Statistics Socio-economic Classification (NS-SEC) work types '
                                           'in the 8 mile buffer area',
             'National Statistics Socio-economic Classification (NS-SEC): Total: All usual residents aged 16 years '
             'and over', 'National Statistics Socio-economic Classification (NS-SEC): L1, L2 and L3 Higher managerial, '
             'administrative and professional occupations', 'Higher managerial, administrative and professional '
             'occupations', 'National Statistics Socio-economic Classification (NS-SEC): L4, L5 and L6 Lower '
             'managerial, administrative and professional occupations', 'Lower managerial, administrative and '
             'professional occupations', 'National Statistics Socio-economic Classification (NS-SEC): L7 Intermediate '
             'occupations', 'Intermediate occupations', 'National Statistics Socio-economic Classification (NS-SEC): '
             'L8 and L9 Small employers and own account workers', 'Small employers and own account workers', 'National '
             'Statistics Socio-economic Classification (NS-SEC): L10 and L11 Lower supervisory and technical '
             'occupations', 'Lower supervisory and technical occupations', 'National Statistics Socio-economic '
             'Classification (NS-SEC): L12 Semi-routine occupations', 'Semi-routine occupations', 'National Statistics '
             'Socio-economic Classification (NS-SEC): L13 Routine occupations', 'Routine occupations', 'National '
             'Statistics Socio-economic Classification (NS-SEC): L14.1 and L14.2 Never worked and long-term unemployed',
             'Never worked and long-term unemployed', 'National Statistics Socio-economic Classification (NS-SEC): '
             'L15 Full-time students', 'Full-time students')

# RELIGION
census_stats(Religion, ProjLSOA, resultsfile, 'Religion of usual residents in the project area',
             'Religion: Total: All usual residents', 'Religion: No religion', 'No religion', 'Religion: Christian',
             'Christian', 'Religion: Buddhist', 'Buddhist', 'Religion: Hindu', 'Hindu', 'Religion: Jewish', 'Jewish',
             'Religion: Muslim', 'Muslim', 'Religion: Sikh', 'Sikh', 'Religion: Other religion', 'Other religion',
             'Religion: Not answered', 'Not answered')

census_stats(Religion, BuffLSOA, resultsfile, 'Religion of usual residents in the 4 mile buffer area',
             'Religion: Total: All usual residents', 'Religion: No religion', 'No religion', 'Religion: Christian',
             'Christian', 'Religion: Buddhist', 'Buddhist', 'Religion: Hindu', 'Hindu', 'Religion: Jewish', 'Jewish',
             'Religion: Muslim', 'Muslim', 'Religion: Sikh', 'Sikh', 'Religion: Other religion', 'Other religion',
             'Religion: Not answered', 'Not answered')

census_stats(Religion, Buff2LSOA, resultsfile, 'Religion of usual residents in the 8 mile buffer area',
             'Religion: Total: All usual residents', 'Religion: No religion', 'No religion', 'Religion: Christian',
             'Christian', 'Religion: Buddhist', 'Buddhist', 'Religion: Hindu', 'Hindu', 'Religion: Jewish', 'Jewish',
             'Religion: Muslim', 'Muslim', 'Religion: Sikh', 'Sikh', 'Religion: Other religion', 'Other religion',
             'Religion: Not answered', 'Not answered')

# TENURE
census_stats(Tenure, ProjLSOA, resultsfile, 'Tenure of households in the project area',
             'Tenure of household: Total: All households', 'Tenure of household: Owned', 'Owned', 'Tenure of household:'
             ' Owned: Owns outright', 'Owned outright', 'Tenure of household: Owned: Owns with a mortgage or loan',
             'Owned with a mortgage or loan', 'Tenure of household: Shared ownership', 'Shared ownership', 'Tenure of '
             'household: Social rented', 'Social rented (all)', 'Tenure of household: Social rented: Rents from '
             'council or Local Authority', 'Social rented from council or Local Authority', 'Tenure of household: '
             'Social rented: Other social rented', 'Social rented (other)', 'Tenure of household: Private rented',
             'Private rented (all)', 'Tenure of household: Private rented: Private landlord or letting agency',
             'Private rented (private landlord or letting agency)', 'Tenure of household: Private rented: Other '
             'private rented', 'Private rented (Other private rented)', 'Tenure of household: Lives rent free',
             'Lives rent free')

census_stats(Tenure, BuffLSOA, resultsfile, 'Tenure of households in the 4 mile buffer area',
             'Tenure of household: Total: All households', 'Tenure of household: Owned', 'Owned', 'Tenure of household:'
             ' Owned: Owns outright', 'Owned outright', 'Tenure of household: Owned: Owns with a mortgage or loan',
             'Owned with a mortgage or loan', 'Tenure of household: Shared ownership', 'Shared ownership', 'Tenure of '
             'household: Social rented', 'Social rented (all)', 'Tenure of household: Social rented: Rents from '
             'council or Local Authority', 'Social rented from council or Local Authority', 'Tenure of household: '
             'Social rented: Other social rented', 'Social rented (other)', 'Tenure of household: Private rented',
             'Private rented (all)', 'Tenure of household: Private rented: Private landlord or letting agency',
             'Private rented (private landlord or letting agency)', 'Tenure of household: Private rented: Other '
             'private rented', 'Private rented (Other private rented)', 'Tenure of household: Lives rent free',
             'Lives rent free')

census_stats(Tenure, Buff2LSOA, resultsfile, 'Tenure of households in the 8 mile buffer area',
             'Tenure of household: Total: All households', 'Tenure of household: Owned', 'Owned', 'Tenure of household:'
             ' Owned: Owns outright', 'Owned outright', 'Tenure of household: Owned: Owns with a mortgage or loan',
             'Owned with a mortgage or loan', 'Tenure of household: Shared ownership', 'Shared ownership', 'Tenure of '
             'household: Social rented', 'Social rented (all)', 'Tenure of household: Social rented: Rents from '
             'council or Local Authority', 'Social rented from council or Local Authority', 'Tenure of household: '
             'Social rented: Other social rented', 'Social rented (other)', 'Tenure of household: Private rented',
             'Private rented (all)', 'Tenure of household: Private rented: Private landlord or letting agency',
             'Private rented (private landlord or letting agency)', 'Tenure of household: Private rented: Other '
             'private rented', 'Private rented (Other private rented)', 'Tenure of household: Lives rent free',
             'Lives rent free')

# IMD
IMD_stats(IMD, ProjLSOA, BuffLSOA, Buff2LSOA, 'Index of Multiple Deprivation (IMD) Decile (where 1 is most deprived '
          '10% of LSOAs)', 'Income Decile (where 1 is most deprived 10% of LSOAs)', 'Income Decile', 'Employment '
          'Decile (where 1 is most deprived 10% of LSOAs)', 'Employment Decile', 'Education, Skills and Training '
          'Decile (where 1 is most deprived 10% of LSOAs)', 'Education skills and training decile',
          'Health Deprivation and Disability Decile (where 1 is most deprived 10% of LSOAs)',
          'Health deprivation and disability decile', 'Crime Decile (where 1 is most deprived 10% of LSOAs)',
          'Crime decile', 'Barriers to Housing and Services Decile (where 1 is most deprived 10% of LSOAs)',
          'Barriers to Housing and Services Decile', 'Living Environment Decile (where 1 is most deprived 10% of'
          ' LSOAs)', 'Living environment decile', 'Income Deprivation Affecting Children Index (IDACI) Decile '
          '(where 1 is most deprived 10% of LSOAs)', 'Income Deprivation Affecting Children Index (IDACI) Decile',
          'Income Deprivation Affecting Older People (IDAOPI) Decile (where 1 is most deprived 10% of LSOAs)',
          'Income Deprivation Affecting Older People (IDAOPI) Decile', 'Children and Young People Sub-domain Decile '
          '(where 1 is most deprived 10% of LSOAs)', 'Adult Skills Sub-domain Decile (where 1 is most deprived 10% of '
          'LSOAs)', 'Geographical Barriers Sub-domain Decile (where 1 is most deprived 10% of LSOAs)', 'Geographical '
          'Barriers Sub-domain Decile', 'Wider Barriers Sub-domain Decile (where 1 is most deprived 10% of LSOAs)',
          'Wider Barriers Sub-domain Decile', 'Indoors Sub-domain Decile (where 1 is most deprived 10% of LSOAs)',
          'Indoors Sub-domain Decile', 'Outdoors Sub-domain Decile (where 1 is most deprived 10% of LSOAs)',
          'Outdoors Sub-domain Decile').to_csv(r'C:/Users/charl/Documents/Essex Wildlife Trust/Population analysis '
                                               r'private/IMD_results.csv')

# POPULATION BY AGE FROM IMD

AllAge = {'Area name': ['TotalEngland']}
AllAges = pd.DataFrame(AllAge)
AllAges['Total population mid 2015'] = IMD['Total population: mid 2015 (excluding prisoners)'].sum()
AllAges['Dependent Children aged 0-15 mid 2015'] = IMD['Dependent Children aged 0-15: mid 2015 ' \
                                                                '(excluding prisoners)'].sum()
AllAges['Population aged 16-59 mid 2015'] = IMD['Population aged 16-59: mid 2015 (excluding prisoners)'].sum()
AllAges['Population aged 60 and over mid 2015'] = IMD['Older population aged 60 and over: mid 2015 ' \
                                                               '(excluding prisoners)'].sum()
AllAges['Working age population 18-59/64'] = IMD['Working age population 18-59/64: for use with Employment ' \
                                                          'Deprivation Domain (excluding prisoners) '].sum()

ProjData = ProjLSOA.join(IMD.set_index('LSOA code (2011)'), on='LSOA21CD', how='left',
                               validate='one_to_one')
ProjAges = {'Area name': ['Project area']}
ProjectAges = pd.DataFrame(ProjAges)
ProjectAges['Total population mid 2015'] = ProjData['Total population: mid 2015 (excluding prisoners)'].sum()
ProjectAges['Dependent Children aged 0-15 mid 2015'] = ProjData['Dependent Children aged 0-15: mid 2015 ' \
                                                                '(excluding prisoners)'].sum()
ProjectAges['Population aged 16-59 mid 2015'] = ProjData['Population aged 16-59: mid 2015 (excluding prisoners)'].sum()
ProjectAges['Population aged 60 and over mid 2015'] = ProjData['Older population aged 60 and over: mid 2015 ' \
                                                               '(excluding prisoners)'].sum()
ProjectAges['Working age population 18-59/64'] = ProjData['Working age population 18-59/64: for use with Employment ' \
                                                          'Deprivation Domain (excluding prisoners) '].sum()

Buffer1Data = BuffLSOA.join(IMD.set_index('LSOA code (2011)'), on='LSOA21CD', how='left',
                               validate='one_to_one')
Buff1Ages = {'Area name': ['4 mile buffer']}
Buffer1Ages = pd.DataFrame(Buff1Ages)
Buffer1Ages['Total population mid 2015'] = Buffer1Data['Total population: mid 2015 (excluding prisoners)'].sum()
Buffer1Ages['Dependent Children aged 0-15 mid 2015'] = Buffer1Data['Dependent Children aged 0-15: mid 2015 ' \
                                                                '(excluding prisoners)'].sum()
Buffer1Ages['Population aged 16-59 mid 2015'] = Buffer1Data['Population aged 16-59: mid 2015 (excluding prisoners)'].sum()
Buffer1Ages['Population aged 60 and over mid 2015'] = Buffer1Data['Older population aged 60 and over: mid 2015 ' \
                                                               '(excluding prisoners)'].sum()
Buffer1Ages['Working age population 18-59/64'] = Buffer1Data['Working age population 18-59/64: for use with Employment ' \
                                                          'Deprivation Domain (excluding prisoners) '].sum()

Buffer2Data = Buff2LSOA.join(IMD.set_index('LSOA code (2011)'), on='LSOA21CD', how='left',
                               validate='one_to_one')
Buff2Ages = {'Area name': ['8 mile buffer']}
Buffer2Ages = pd.DataFrame(Buff2Ages)
Buffer2Ages['Total population mid 2015'] = Buffer2Data['Total population: mid 2015 (excluding prisoners)'].sum()
Buffer2Ages['Dependent Children aged 0-15 mid 2015'] = Buffer2Data['Dependent Children aged 0-15: mid 2015 ' \
                                                                '(excluding prisoners)'].sum()
Buffer2Ages['Population aged 16-59 mid 2015'] = Buffer2Data['Population aged 16-59: mid 2015 (excluding prisoners)'].sum()
Buffer2Ages['Population aged 60 and over mid 2015'] = Buffer2Data['Older population aged 60 and over: mid 2015 ' \
                                                               '(excluding prisoners)'].sum()
Buffer2Ages['Working age population 18-59/64'] = Buffer2Data['Working age population 18-59/64: for use with Employment ' \
                                                          'Deprivation Domain (excluding prisoners) '].sum()

Ages = pd.concat([AllAges, ProjectAges, Buffer1Ages, Buffer2Ages], ignore_index=True)
Ages['Percentage of dependent children 0-15'] = (Ages['Dependent Children aged 0-15 mid 2015']/Ages['Total population '
                                                                                                    'mid 2015'])*100
Ages['Percentage of population aged 16-59'] = (Ages['Population aged 16-59 mid 2015']/Ages['Total population '
                                                                                                    'mid 2015'])*100
Ages['Percentage of population aged 60 and over'] = (Ages['Population aged 60 and over mid 2015']/Ages['Total '
                                                                                                       'population '
                                                                                                    'mid 2015'])*100
Ages['Percentage of population working age'] = (Ages['Working age population 18-59/64']/Ages['Total '
                                                                                                       'population '
                                                                                                    'mid 2015'])*100
EngDep = float(Ages.loc[Ages['Area name'] == 'TotalEngland', 'Percentage of dependent children 0-15'])
Eng16 = float(Ages.loc[Ages['Area name'] == 'TotalEngland', 'Percentage of population aged 16-59'])
Eng60 = float(Ages.loc[Ages['Area name'] == 'TotalEngland', 'Percentage of population aged 60 and over'])
EngEmp = float(Ages.loc[Ages['Area name'] == 'TotalEngland', 'Percentage of population working age'])

Ages['Ratio dependent children compared to England'] = Ages['Percentage of dependent children 0-15']/EngDep

Ages['Ratio 16-59 compared to England'] = Ages['Percentage of population aged 16-59']/Eng16

Ages['Ratio 60 and over compared to England'] = Ages['Percentage of population aged 60 and over']/Eng60

Ages['Ratio working age compared to England'] = Ages['Percentage of population working age']/EngEmp

Ages.to_csv(r'C:/Users/charl/Documents/Essex Wildlife Trust/Population analysis private/Ages_from_IMD.csv')
